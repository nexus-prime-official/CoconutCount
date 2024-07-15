import streamlit as st
import torch
from torchvision import transforms
from PIL import Image
import numpy as np

@st.catche_data
def load_model():
    model = torch.model("D:\GitHub\CoconutCount\model-4.pth")
    model.eval()
    return model

model = load_model()
def preprocess_image(image):
    preprocess = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ])
    image = preprocess(image)
    image = image.unsqueeze(0)  # Add batch dimension
    return image

# Streamlit app
st.title("Object Counting App")

uploaded_file = st.file_uploader("Choose an image...", type=["tiff"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    st.write("")
    st.write("Counting objects...")

    # Preprocess the image
    image_tensor = preprocess_image(image)

    # Count objects
    with torch.no_grad():
        count = model(image_tensor).item()  # Perform counting using your model

    # Display the result
    st.write(f'Number of objects detected: {count}')