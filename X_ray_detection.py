import streamlit as st
from transformers import pipeline
from PIL import Image

# Load the image classification pipeline
image_classifier = pipeline("image-classification", model="nickmuchi/vit-finetuned-chest-xray-pneumonia")

def main():
    st.title("Pneumonia X Ray Detection")
    st.write("Upload an image of your chest X ray")

    # Allow user to upload an image
    uploaded_image = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_image is not None:
        # Display the uploaded image
        image = Image.open(uploaded_image)
        st.image(image, caption="Uploaded Image", use_column_width=True)

        # Perform image classification
        predictions = image_classifier(image)

        # Display the classification results
        st.subheader("Classification Results:")
        for prediction in predictions:
            st.write(f"Label: {prediction['label']}, Confidence: {prediction['score']}")

if __name__ == "__main__":
    main()
