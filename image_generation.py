# image_generator.py
import replicate
import os
from dotenv import load_dotenv

load_dotenv()
os.environ["REPLICATE_API_TOKEN"] = os.getenv("REPLICATE_API_TOKEN")

def generate_flux_image(prompt: str, save_path: str = "output.jpg") -> str:
    print(f"🎨 Generating image with prompt: {prompt}")

    try:
        inputs = {
            "prompt": prompt,
            "prompt_upsampling": True
        }

        output = replicate.run("black-forest-labs/flux-1.1-pro", input=inputs)

        # Output is a URL, download it
        import requests
        img_data = requests.get(output[0]).content
        with open(save_path, "wb") as f:
            f.write(img_data)

        print(f"✅ Image saved: {save_path}")
        return save_path

    except Exception as e:
        print(f"❌ Error generating image: {e}")
        return None
