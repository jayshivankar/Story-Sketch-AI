# image_generator.py
import os
from huggingface_hub import InferenceClient
from dotenv import load_dotenv

load_dotenv()
HF_TOKEN = os.getenv("HF_TOKEN")

client = InferenceClient(
    provider="together",
    api_key=HF_TOKEN,
)

def generate_flux_image(prompt: str, save_path: str = "output.png") -> str:
    try:
        print(f"🎨 Generating image from text: {prompt}")

        # Generate image using Together's hosted FLUX model
        image = client.text_to_image(
            prompt=prompt,
            model="black-forest-labs/FLUX.1-dev"
        )

        # Save to file
        image.save(save_path)
        print(f"✅ Image saved to {save_path}")
        return save_path

    except Exception as e:
        print(f"❌ Error generating image: {e}")
        return None
