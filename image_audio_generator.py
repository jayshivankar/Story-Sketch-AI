# image_audio_generator.py
import os
from pathlib import Path
from gtts import gTTS
from image_generation import generate_flux_image
from moviepy import ImageClip, AudioFileClip

# Ensure folders exist
Path("data/images").mkdir(parents=True, exist_ok=True)
Path("data/audio").mkdir(parents=True, exist_ok=True)
Path("data/videos").mkdir(parents=True, exist_ok=True)

def generate_scene_image(prompt: str, index: int) -> str:
    img_path = generate_flux_image(prompt, index)  # Updated
    return img_path

def generate_scene_audio(prompt: str, index: int) -> str:
    path = f"data/audio/scene_{index:02}.mp3"
    tts = gTTS(text=prompt, lang="en")
    tts.save(path)
    print(f"🔊 Audio saved: {path}")
    return path

def make_scene_video(index: int, image_path: str, audio_path: str) -> str:
    video_path = f"data/videos/scene_{index:02}.mp4"
    audio = AudioFileClip(audio_path)
    clip = ImageClip(image_path).with_duration(audio.duration).with_audio(audio)
    clip.write_videofile(video_path, fps=24, logger=None)
    print(f"🎬 Video created: {video_path}")
    return video_path

def generate_all_assets(scene_prompts: list[str]):
    for i, prompt in enumerate(scene_prompts, 1):
        print(f"\n📍 Processing Scene {i}")
        img = generate_scene_image(prompt, i)
        aud = generate_scene_audio(prompt, i)

        if img and os.path.exists(img):
            make_scene_video(i, img, aud)
        else:
            print(f"⚠️ Skipping Scene {i} due to missing image")

    print("\n✅ All scenes processed and saved.")
