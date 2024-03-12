# Image Whisper
## Image Processing and Text-to-Speech App

Image Whisper is a Streamlit web application designed for image processing, text extraction, and text-to-speech (TTS) conversion. It provides users with the capability to upload images, detect objects within them, extract text, and generate audio narrations based on the extracted text.

## Installation

To run Image Whisper, ensure you have the necessary dependencies installed. You can do this via pip and npm:

```bash
pip install -r requirements.txt
npm install localtunnel
sudo apt-get install espeak
```

The required Python libraries include:

- `timm`
- `phonemizer`
- `inflect`
- `streamlit`
- `Pillow`
- `torch`
- `transformers`
- `matplotlib`
- `py-espeak-ng`

## Overview

Image Whisper consists of two primary components:

1. **Object Detection**: Utilizes the DETR (DEtection TRansformer) model with a ResNet-50 backbone for end-to-end object detection. This model is trained on the COCO 2017 dataset and is capable of detecting a wide range of objects in images.

2. **Text-to-Speech (TTS)**: Employs the VITS (Conditional Variational Autoencoder with Adversarial Learning) model for end-to-end text-to-speech synthesis. VITS predicts speech waveforms conditioned on input text sequences and is trained on the LJ Speech dataset.

## Workflow

1. **Upload Image**: Users upload an image using the provided file uploader in the web interface.
2. **Object Detection**: The uploaded image undergoes object detection using a pre-trained DETR model, identifying objects within the image.
3. **Text Extraction**: Text is extracted from the detected objects using optical character recognition (OCR) technology.
4. **Text Explanation**: Extracted text is analyzed and explained in natural language, providing additional context or details.
5. **Audio Output**: The explained text is converted to audio using text-to-speech (TTS) technology, delivering an audio description of the text in the image.
6. **Display Results**: Processed image, explained text, and audio output are presented to the user through the web interface.

   

## Architecture and Model Details

### DETR Model (End-to-End Object Detection)

The DETR model is an end-to-end object detection model based on a transformer architecture. Trained on the COCO 2017 object detection dataset, DETR is proficient in detecting diverse objects within images.
![detr_architecture](https://github.com/chethanhn29/Large-Language-Models/assets/110838853/355b6dbe-d4b4-42fe-a4b8-554c797d8703)

### VITS Model (Conditional Variational Autoencoder for TTS)

VITS is a conditional variational autoencoder (VAE) tailored for end-to-end text-to-speech synthesis. Trained on the LJ Speech dataset, VITS predicts speech waveforms conditioned on input text sequences.

## Project Files

- `app.py`: Main file containing the Streamlit web application code.
- `helper.py`: Contains helper functions utilized within the application.
- `predictions.py`: Module comprising functions for object detection, text extraction, and natural language processing.
- `get_predictions.ipynb`: Jupyter Notebook for running the Streamlit application in Google Colab.

## Running the Application

### Google Colab

To run the application in Google Colab:

1. Open `get_predictions.ipynb` in Google Colab.
2. Execute the code cells to install required libraries and start the Streamlit server.
3. Access the application via the generated localtunnel URL.

### Local Machine

To run the application locally:

1. Ensure all required libraries are installed as specified in the installation instructions.
2. Run the `app.py` file using Streamlit:

   ```bash
   streamlit run app.py
   ```

3. Access the application in your web browser at `http://localhost:8501`.

## Notes

- Ensure necessary Python and npm packages are installed prior to running the application.
- In Colab, the public IP address serves as the password for localtunnel. Provide this when prompted.
- For audio output, ensure the `espeak` package is installed on your system.
```






       +-------------------------------------+
       |        Web Interface                |
       +-------------------------------------+
                      |
                      v
       +-------------------------------------+
       |      Object Detection Model         |
       |   (DETR with ResNet-50 backbone)   |
       +-------------------------------------+
                      |
                      v
       +-------------------------------------+
       |          Text Extraction            |
       |         (OCR Module)                |
       +-------------------------------------+
                      |
                      v
       +-------------------------------------+
       |        Text Explanation             |
       +-------------------------------------+
                      |
                      v
       +-------------------------------------+
       |   Text-to-Speech (TTS Module)       |
       |    (VITS: Conditional VAE model)    |
       +-------------------------------------+
                      |
                      v
       +-------------------------------------+
       |        Audio Output                 |
       +-------------------------------------+



