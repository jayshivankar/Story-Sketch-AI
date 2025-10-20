from llm.llm_helper import llm
from langchain_core.messages import HumanMessage

def generate_story(prompt: str) -> str:
    story_prompt = f"""
You are a creative children's story writer.
Write a short, engaging, and fun story for kids (ages 6–10) based on:
"{prompt}"

Requirements:
- Use simple and imaginative language
- Include adventure, emotion, and a positive message
- Start strong, end happily
- 2–4 lines per paragraph
No preamble or explanation.
"""
    try:
        response = llm.invoke([HumanMessage(content=story_prompt)])
        return response.content.strip()
    except Exception as e:
        raise RuntimeError(f"Story generation failed: {e}")

def extract_scenes(story_text: str) -> list[str]:
    scene_prompt = f"""
Break this children's story into vivid, visually descriptive scenes.

Each line should describe one major visual moment (Scene 1:, Scene 2:, etc.)
Each scene must include the main character's name and what they are.

Story:
\"\"\"{story_text}\"\"\"
"""
    try:
        response = llm.invoke([HumanMessage(content=scene_prompt)])
        raw_output = response.content.strip()
        scenes = [
            line.split(":", 1)[1].strip()
            for line in raw_output.splitlines()
            if line.lower().startswith("scene")
        ]
        if not scenes:
            raise ValueError("No scenes extracted.")
        return scenes
    except Exception as e:
        raise RuntimeError(f"Scene extraction failed: {e}")
