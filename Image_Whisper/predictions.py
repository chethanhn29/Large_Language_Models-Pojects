from PIL import Image, ImageDraw
from helper import summarize_predictions_natural_language, render_results_in_image
from transformers import pipeline
from tokenizers import Tokenizer, Encoding
from tokenizers import decoders
from tokenizers import models
from tokenizers import normalizers
from tokenizers import pre_tokenizers
from tokenizers import processors

# Load object detection pipeline
object_detection_pipe = pipeline("object-detection", model="facebook/detr-resnet-50")

# Load text-to-speech pipeline
tts_pipe = pipeline("text-to-speech", model="kakao-enterprise/vits-ljs")

def get_predictions(uploaded_image):
    pil_image = Image.open(uploaded_image)

    # Perform object detection
    pipeline_output = object_detection_pipe(pil_image)
    processed_image = render_results_in_image(pil_image, pipeline_output)

    # Summarize predictions
    text = summarize_predictions_natural_language(pipeline_output)
    corrected_text = correct_text(text)

      # Generate audio from text
    narrated_text = tts_pipe(corrected_text)
    audio_data = narrated_text["audio"][0]
    sample_rate = narrated_text["sampling_rate"]

    return processed_image,corrected_text, (sample_rate, audio_data)


def correct_text(text):
    # Rule-based correction
    # Example: "there are one horse" -> "there is one horse"
    if "there are one" in text:
        text = text.replace("there are one", "there is one")
    return text