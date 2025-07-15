
import replicate
import os
from dotenv import load_dotenv


load_dotenv()
os.environ["REPLICATE_API_TOKEN"] = os.getenv("REPLICATE_API_TOKEN")

def generate_flux_image(prompt: str, save_path: str = "output.jpg") -> str:
    print(f"🎨 Generating image with prompt: {prompt}")

    try:
        # Input for Flux model
        inputs = {
            "prompt": prompt,
            "prompt_upsampling": True
        }

        # Run the model
        output = replicate.run("black-forest-labs/flux-1.1-pro", input=inputs)

        # Save output image
        with open(save_path, "wb") as f:
            f.write(output.read())

        print(f"✅ Image saved as {save_path}")
        return save_path

    except Exception as e:
        print(f"❌ Failed to generate image: {e}")
        return None

# Example use
if __name__ == "__main__":
    test_prompt = "Rosie the rabbit and Ping the panda sat together in their cozy bamboo forest home, surrounded by papers, ropes, and cans, with a spark of excitement in their eyes."
    generate_flux_image(test_prompt, save_path="rosie_owl.png")
