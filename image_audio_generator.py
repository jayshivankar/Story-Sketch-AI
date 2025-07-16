import os
from pathlib import Path
from gtts import gTTS
from moviepy import ImageClip, AudioFileClip
from image_generation import generate_flux_image

Path("data/images").mkdir(parents=True, exist_ok=True)
Path("data/audio").mkdir(parents=True, exist_ok=True)
Path("data/videos").mkdir(parents=True, exist_ok=True)

def generate_scene_image(prompt :str, index :int) -> str:
    path = f"data/images/scene_{index:02}.png"
    generate_flux_image(prompt,path)
    return path

def generate_scene_audio(prompt :str, index :int) -> str:
    path = f"data/audio/scene_{index:02}.mp3"
    tts = gTTS(text=prompt,lang="en")
    tts.save(path)
    return path

def generate_all_assets()