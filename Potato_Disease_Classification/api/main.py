from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import numpy as np
from io import BytesIO
from PIL import Image
import tensorflow as tf

app = FastAPI()

# Allow requests from frontend (e.g., http://localhost:5173)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace "*" with frontend URL in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load your trained model
Model = tf.keras.models.load_model('my_model.keras')
class_names = ['Potato___Early_blight', 'Potato___Late_blight', 'Potato___healthy']


@app.get("/")
async def ping():
    return {"message": "Hello, I am alive!"}


def read_file_as_image(data) -> np.ndarray:
    image = np.array(Image.open(BytesIO(data)))
    return image


@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    # Read and preprocess image
    image = read_file_as_image(await file.read())
    image = tf.image.resize(image, (256, 256))  # Match your model's expected input
    image = np.expand_dims(image, axis=0)

    # Predict
    predictions = Model.predict(image)
    predicted_class = class_names[np.argmax(predictions[0])]
    confidence = float(np.max(predictions[0]))

    # Return structured response
    return {
        "class": predicted_class,
        "confidence": confidence
    }
