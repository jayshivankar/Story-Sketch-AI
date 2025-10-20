import replicate
import os

os.environ["REPLICATE_API_TOKEN"] = os.getenv("REPLICATE_API_TOKEN")

def generate_flux_image(prompt: str, index: int, save_dir="data/images") -> str:
    """Generate an image using Replicate’s Flux model."""
    try:
        print(f"🎨 Generating image for Scene {index}: {prompt}")
        output = replicate.run("black-forest-labs/flux-dev", input={"prompt": prompt})
        os.makedirs(save_dir, exist_ok=True)

        image_paths = []
        for i, item in enumerate(output):
            filename = f"scene_{index:02}_{i}.webp" if len(output) > 1 else f"scene_{index:02}.webp"
            save_path = os.path.join(save_dir, filename)
            with open(save_path, "wb") as f:
                f.write(item.read())
            image_paths.append(save_path)
            print(f"✅ Saved image: {save_path}")

        return image_paths[0] if len(image_paths) == 1 else image_paths
    except Exception as e:
        print(f"❌ Image generation failed: {e}")
        return None
