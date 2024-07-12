import google.generativeai as genai
import os
from PIL import Image
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

model = genai.GenerativeModel('models/gemini-pro-vision')

# check https://cloud.google.com/vertex-ai/generative-ai/docs/multimodal/send-multimodal-prompts 
# check https://ai.google.dev/gemini-api/docs/get-started/python



def prompt_gemini(image_path, onto_prompt):
    # Load an image from file
	image = Image.open(image_path)

	response = model.generate_content([onto_prompt, img], stream=True)
	response.resolve()

    return response.text



