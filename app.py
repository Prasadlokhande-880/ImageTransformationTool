import streamlit as st
import cv2
import numpy as np
from PIL import Image
import transformations  # Ensure this file exists in the same directory with updated functions

# Title of the app
st.title("Image Transformation Tool")

# Sidebar for navigation
st.sidebar.header("Transformation Options")
st.sidebar.info("Choose an image and apply various transformations.")

# File uploader
uploaded_file = st.file_uploader("Upload an image (JPG, PNG, JPEG)", type=["jpg", "png", "jpeg"])

if uploaded_file:
    try:
        # Load and display the uploaded image
        image = np.array(Image.open(uploaded_file))
        st.subheader("Uploaded Image")
        st.image(image, caption="Original Image", use_column_width=True)

        # Transformation selection
        st.subheader("Transformation Settings")
        transformation = st.radio(
            "Choose a transformation",
            ["Shift", "Resize", "Rotate", "Skew"]
        )

        # Transformation settings
        if transformation == "Shift":
            shift_x = st.sidebar.slider("Shift X (pixels)", -200, 200, 50)
            shift_y = st.sidebar.slider("Shift Y (pixels)", -200, 200, 50)
            transformed_image = transformations.shift_image(image, shift_x, shift_y)

        elif transformation == "Resize":
            factor_x = st.sidebar.slider("Resize Factor X", 0.1, 3.0, 1.0)
            factor_y = st.sidebar.slider("Resize Factor Y", 0.1, 3.0, 1.0)
            transformed_image = transformations.resize_image(image, factor_x, factor_y)

        elif transformation == "Rotate":
            angle = st.sidebar.slider("Rotation Angle (degrees)", 0, 360, 45)
            transformed_image = transformations.rotate_image(image, angle)

        elif transformation == "Skew":
            shear_x = st.sidebar.slider("Shear X Factor", -1.0, 1.0, 0.0)
            shear_y = st.sidebar.slider("Shear Y Factor", -1.0, 1.0, 0.0)
            transformed_image = transformations.skew_image(image, shear_x, shear_y)

        # Display the transformed image
        st.subheader(f"Transformed Image ({transformation})")
        st.image(transformed_image, caption=f"Result of {transformation}", use_column_width=True)

    except Exception as e:
        st.error(f"Error occurred: {e}")
else:
    st.info("Upload an image using the file uploader in the sidebar to start!")
