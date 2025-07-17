# image_generator.py
import replicate
import os
import requests
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

        # Run the model
        output = replicate.run("black-forest-labs/flux-1.1-pro", input=inputs)

        # Handle output format
        if isinstance(output, list):
            img_url = output[0]
        elif isinstance(output, str):
            img_url = output
        else:
            raise ValueError("Unexpected output type from replicate.run()")

        # Download and save the image
        img_data = requests.get(img_url).content
        with open(save_path, "wb") as f:
            f.write(img_data)

        print(f"✅ Image saved: {save_path}")
        return save_path

    except Exception as e:
        print(f"❌ Error generating image: {e}")
        return None


