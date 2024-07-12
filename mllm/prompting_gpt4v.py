#this code is adapted using openAI docs https://platform.openai.com/docs/guides/vision
from openai import OpenAI
import requests
import base64
# Set your OpenAI API key
openai.api_key = "YOUR_OPENAI_API_KEY"
# Initializing OpenAI client - see https://platform.openai.com/docs/quickstart?context=python

client = OpenAI()

def prompt_gpt4_vision(image_path, onto_prompt):
    # Read the image file and encode it in base64 format
    with open(image_path, "rb") as image_file:
        image_data = image_file.read()
        image_base64 = base64.b64encode(image_data).decode("utf-8")

    response = client.chat.completions.create(
    model="gpt-4-vision-preview",
    "messages": [
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": onto_prompt
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{base64_image}"
                    }
                }
            ]
        }
    ],
        max_tokens=300,
        top_p=0.1
    )

    return response.choices[0].message.content





