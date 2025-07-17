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

        output = replicate.run("black-forest-labs/flux-1.1-pro", input=inputs)
        print(f"🔍 Raw output from Replicate: {output}")

        #  Fix: If output is an iterator or a FileOutput object, convert to list
        if hasattr(output, '__iter__') and not isinstance(output, (str, bytes)):
            output = list(output)

        if isinstance(output, list) and len(output) > 0:
            img_url = output[0]
        elif isinstance(output, str):
            img_url = output
        else:
            raise ValueError(f"Unexpected output type from replicate.run(): {type(output)}")

        # Save image from URL
        img_data = requests.get(img_url).content
        with open(save_path, "wb") as f:
            f.write(img_data)

        print(f"✅ Image saved: {save_path}")
        return save_path

    except Exception as e:
        print(f"❌ Error generating image: {e}")
        return None

