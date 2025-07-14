import replicate
import os
import requests
from dotenv import load_dotenv

load_dotenv()
os.environ["REPLICATE_API_TOKEN"] = os.getenv("REPLICATE_API_TOKEN")

MODEL = "lucataco/sdxl:8cf5e2c0f24061b627eaa9b21fa60a84d913fd0c5cecf65c6f5818f5fc6c0c60"


def generate_and_save_image(prompt: str, save_path: str = "scene.png") -> str:
    print(f"🎨 Generating image for: {prompt}")

    output = replicate.run(
        MODEL,
        input={"prompt": prompt}
    )

    if isinstance(output, list) and output:
        image_url = output[0]
        try:
            img_data = requests.get(image_url).content
            with open(save_path, "wb") as f:
                f.write(img_data)
            print(f"✅ Image saved to {save_path}")
            return save_path
        except Exception as e:
            print(f"❌ Failed to download image: {e}")
            return None
    else:
        print("❌ No image generated.")
        return None

if __name__ == "__main__":
    prompt = "Josh the panda exploring an alien planet, in children's illustration style"
    generate_and_save_image(prompt, save_path="josh_alien_planet.png")
