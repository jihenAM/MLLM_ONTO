from PIL import Image
import torch
from transformers import AutoProcessor, LlavaForConditionalGeneration


model_id = "llava-hf/llava-v1.6-34b-hf"
processor = AutoProcessor.from_pretrained(model_id)
model = LlavaForConditionalGeneration.from_pretrained(
    model_id,
    torch_dtype=torch.float16,
    device_map="auto"
)

def prompt_llava(image_path, onto_prompt):

    image = Image.open(image_path).convert("RGB")
    prompt_with_tag = f"<image>\n{onto_prompt}"
    inputs = processor(prompt_with_tag, images=image, return_tensors="pt").to(model.device)
    output = model.generate(**inputs, max_new_tokens=512)
    response = processor.batch_decode(output, skip_special_tokens=True)[0]

    return response
