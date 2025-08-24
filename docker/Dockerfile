# syntax=docker/dockerfile:1

ARG PYTHON_VERSION=3.10.18
FROM python:${PYTHON_VERSION}-slim as base

# Prevent Python from writing pyc files
ENV PYTHONDONTWRITEBYTECODE=1
# Prevent Python stdout/stderr buffering
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Create a non-privileged user that the app will run under
# UID is configurable
ARG UID=10001
RUN adduser \
    --disabled-password \
    --gecos "" \
    --home "/app" \
    --shell "/sbin/nologin" \
    --uid "${UID}" \
    appuser

# Create .streamlit directory and set permissions
RUN mkdir -p /app/.streamlit && chown -R appuser:appuser /app

# Install dependencies
RUN --mount=type=cache,target=/root/.cache/pip \
    --mount=type=bind,source=requirements.txt,target=requirements.txt \
    pip install --no-cache-dir -r requirements.txt

# Switch to the non-privileged user
USER appuser

# Copy source code AFTER dependencies to leverage Docker cache
COPY --chown=appuser:appuser . .

# Expose Streamlit port
EXPOSE 8501

# Run the application
CMD ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]
