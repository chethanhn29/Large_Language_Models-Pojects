
# Image Whisper
## Image Processing and Text-to-Speech App

This is a Streamlit web application for processing images, extracting text, and converting it to audio using text-to-speech (TTS) technology. The application consists of three stages: object detection, text explanation, and audio output.

## Installation

To run the application, you need to install the required libraries. You can do this using pip and npm:

```bash
pip install -r requirements.txt
npm install localtunnel
sudo apt-get install espeak
```

The required Python libraries are:

- `timm`
- `phonemizer`
- `inflect`
- `streamlit`
- `Pillow`
- `torch`
- `transformers`
- `matplotlib`
- `py-espeak-ng`

## How it Works

### Workflow

1. **Upload Image**: Users upload an image using the file uploader provided in the web interface.
2. **Object Detection**: The uploaded image is passed through a pre-trained object detection model to identify objects present in the image.
3. **Text Extraction**: The text is extracted from the detected objects in the image using optical character recognition (OCR) technology.
4. **Text Explanation**: The extracted text is analyzed and explained in natural language to provide additional context or details.
5. **Audio Output**: The explained text is converted to audio using text-to-speech (TTS) technology, providing an audio description of the text in the image.
6. **Display Results**: The processed image, explained text, and audio output are displayed to the user via the web interface.

       +-------------------+
       |   Web Interface   |
       +-------------------+
                 |
                 v
       +-------------------+
       | Object Detection  |
       |      Model        |
       +-------------------+
                 |
                 v
       +-------------------+
       | Text Extraction   |
       |   (OCR Module)    |
       +-------------------+
                 |
                 v
       +-------------------+
       | Text Explanation  |
       +-------------------+
                 |
                 v
       +-------------------+
       | Text-to-Speech    |
       |    (TTS Module)   |
       +-------------------+
                 |
                 v
       +-------------------+
       |   Audio Output    |
       +-------------------+

### Project Files

- `app.py`: Main file containing the Streamlit web application code.
- `helper.py`: Helper functions used in the application.
- `predictions.py`: Module containing functions for object detection, text extraction, and natural language processing.
- `get_predictions.ipynb`: Jupyter Notebook file for running the Streamlit application in Google Colab.

## Running the Application

### Google Colab

To run the application in Google Colab, follow these steps:

1. Open `get_predictions.ipynb` in Google Colab.
2. Run the code cells in the notebook to install the required libraries and start the Streamlit server.
3. Access the application via the generated localtunnel URL.

### Local Machine

To run the application on a local machine:

1. Ensure you have the required libraries installed as mentioned in the installation instructions.
2. Run the `app.py` file using Streamlit:

   ```bash
   streamlit run app.py
   ```

3. Access the application in your web browser at `http://localhost:8501`.

## Notes

- Ensure that the necessary Python and npm packages are installed before running the application.
- In Colab, the public IP address is used as the password for localtunnel. Ensure that you provide this when prompted.
- For audio output, ensure that the `espeak` package is installed on your system.


