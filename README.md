# 🥔 Potato Disease Classification Web App and deploying using **Docker** and **AWS ECS**

## 📌 Overview
This project implements a **Potato Disease Classification** system using a **Convolutional Neural Network (CNN)** trained on a Kaggle dataset.  
The complete pipeline includes:
- **Model training** in TensorFlow (via Jupyter Notebook)
- **Streamlit app** for an interactive user interface

---

## 📂 Dataset
- **Source:** [Kaggle Potato Leaf Disease Dataset](https://www.kaggle.com/datasets/arjuntejaswi/plant-village)
- Contains potato leaf images labeled as:
  - Healthy
  - Early Blight
  - Late Blight

---

## ⚙️ Model Training

### 1️⃣ Data Loading
- Loaded dataset into a `tf.data.Dataset` object for efficient preprocessing.

### 2️⃣ Preprocessing Pipelines
- **Resizing & Rescaling** – Converts all images to `(256, 256)` and normalizes pixel values to `[0, 1]`.
- **Data Augmentation** – Random flips and rotations to make the model robust to image orientation changes.

### 3️⃣ Model
- CNN-based classifier implemented in TensorFlow/Keras.

### 4️⃣ Saving the Model
- Model is saved in `.keras` format after training:
  ```python
  model.save("my_model.keras")

# deployment of a Convolutional Neural Network (CNN) model**  using **Docker** and **AWS ECS**.

## 🚀 Live Demo
You can try the deployed application here:  
👉 [Potato Disease Classifier](http://43.204.141.23:8501/)

---
## 4️⃣ Use the Application

- Open your browser and go to the Streamlit URL.
- Upload a potato leaf image (JPG/PNG).
- The classification result will be displayed.
