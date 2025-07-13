# generate_image.py
import requests
import os
from dotenv import load_dotenv

load_dotenv()
HF_API_TOKEN = os.getenv("HF_API_TOKEN")

# ✅ A working model for inference
API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-2-1"
headers = {
    "Authorization": f"Bearer {HF_API_TOKEN}",
    "Content-Type": "application/json"
}

def generate_image(prompt: str, save_path="generated_image.png"):
    payload = {
        "inputs": prompt,
        "options": {
            "wait_for_model": True
        }
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

# Example usage
if __name__ == "__main__":
    prompt = "Josh the panda floats in space wearing an astronaut suit, in children's illustration style"
    generate_image(prompt, save_path="josh_space.png")
