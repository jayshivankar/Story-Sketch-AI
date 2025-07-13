# generate_image.py
import requests
import os
from dotenv import load_dotenv

load_dotenv()
HF_API_TOKEN = os.getenv("HF_API_TOKEN")

API_URL = "https://api-inference.huggingface.co/models/PixArt-alpha/PixArt-XL-2-1024-MS"
headers = {
    "Authorization": f"Bearer {HF_API_TOKEN}",
    "Content-Type": "application/json"
}

def generate_pixart_image(prompt: str, save_path="generated_image.png"):
    payload = {
        "inputs": prompt,
        "parameters": {"guidance_scale": 6.0, "num_inference_steps": 30}
    }

    response = requests.post(API_URL, headers=headers, json=payload)

    if response.status_code == 200:
        with open(save_path, "wb") as f:
            f.write(response.content)
        print(f"✅ Image saved to {save_path}")
        return save_path
    else:
        print(f"❌ Error {response.status_code}: {response.text}")
        return None
