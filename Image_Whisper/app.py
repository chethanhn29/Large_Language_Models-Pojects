import streamlit as st
from PIL import Image
from predictions import get_predictions

def main():
    st.title("Image Whisper App")

    uploaded_image = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

    if uploaded_image is not None:
        st.subheader("Uploaded Image")
        st.image(uploaded_image, use_column_width=True)

        if st.button("Submit"):
            processed_image, text, audio = get_predictions(uploaded_image)

            st.subheader("Detected Objects")
            st.image(processed_image, use_column_width=True)

            st.subheader("Predicted Text")
            st.write(text)

            st.subheader("Audio Output")
            if isinstance(audio, tuple):
                sample_rate, audio_data = audio
                st.audio(audio_data, format='audio/wav', sample_rate=sample_rate)
            else:
                st.audio(audio, format='audio/wav')

if __name__ == '__main__':
    main()
