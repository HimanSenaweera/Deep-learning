import streamlit as st
import numpy as np
import tensorflow as tf
from PIL import Image
from io import BytesIO

st.set_page_config(page_title="Potato Disease Classifier", page_icon="🥔", layout="centered")

Model = tf.keras.models.load_model("new2.keras", compile=False)
class_names = ["Potato___Early_blight", "Potato___Late_blight", "Potato___healthy"]


st.markdown("""
<style>
/* page background */
[data-testid="stAppViewContainer"] {
  background-image: url("https://wallpapers.com/images/hd/plain-dark-green-wallpaper-4py2q8q4fvne42p7.jpg");
  background-size: cover;
  background-position: center;
}

</style>
""", unsafe_allow_html=True)


def read_file_as_image(data):
    img = Image.open(BytesIO(data))
    return np.array(img)

def preprocess(img_arr):
    x = np.expand_dims(img_arr, axis=0)  
    return x

def predict(image_bytes):
    global img_arr 
    img_arr= read_file_as_image(image_bytes)
    img_arr = np.expand_dims(img_arr, axis=0)
    
    predictions = Model.predict(img_arr)
    
    predicted_class = class_names[np.argmax(predictions[0])]
    confidence = float(np.max(predictions[0]))
    
    return predicted_class,confidence

uploaded_file = st.file_uploader("", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    prediction,confidence_ = predict(uploaded_file.read())
    st.image(img_arr)
    st.success(f"Prediction: {prediction} ")

else:
    st.info("Upload a image to get a prediction.")