# image_generator.py
import replicate
import os

# Your Replicate API key
os.environ["REPLICATE_API_TOKEN"] = os.getenv("REPLICATE_API_TOKEN")

def generate_flux_image(prompt: str, index: int, save_dir="data/images") -> str:
    try:
        print(f"🎨 Generating image with Replicate: {prompt}")
        input = {
            "prompt": prompt
        }

        output = replicate.run("black-forest-labs/flux-dev", input=input)

        os.makedirs(save_dir, exist_ok=True)
        image_paths = []

        for i, item in enumerate(output):
            filename = f"scene_{index:02}_{i}.webp" if len(output) > 1 else f"scene_{index:02}.webp"
            save_path = os.path.join(save_dir, filename)

            with open(save_path, "wb") as file:
                file.write(item.read())
            print(f"✅ Image saved: {save_path}")
            image_paths.append(save_path)

        return image_paths[0] if len(image_paths) == 1 else image_paths

    except Exception as e:
        print(f"❌ Error generating image: {e}")
        return None
