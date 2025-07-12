import gradio as gr
import numpy as np
from PIL import Image
from transformers import BlipProcessor, BlipForQuestionAnswering

# Load BLIP processor and model
processor = BlipProcessor.from_pretrained("Salesforce/blip-vqa-base")
model = BlipForQuestionAnswering.from_pretrained("Salesforce/blip-vqa-base")

# Define the function for Visual Question Answering
def VQA(input_image: np.ndarray, question):
    # Convert numpy array to PIL Image and convert to RGB
    raw_image = Image.fromarray(input_image).convert('RGB')

    # Prepare the inputs for the model
    inputs = processor(raw_image, question, return_tensors="pt")

    # Generate the answer using the model
    outputs = model.generate(**inputs, max_length=100)

    # Decode the generated tokens to text and store it into `output`
    answer = processor.decode(outputs[0], skip_special_tokens=True)

    return answer

# Create a Gradio interface
iface = gr.Interface(
    fn=VQA, 
    inputs=[
        gr.Image(label="Input image:"),
        gr.Textbox(label="Question:", placeholder="Type your question here...")
    ],
    outputs="text",
    title="Visual Question Answering",
    description="This is a simple web app for VQA using BLIP model from Salesforce.\nUpload the image file:"
)

# Launch the Gradio app
iface.launch()