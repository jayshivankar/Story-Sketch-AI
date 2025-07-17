
from Llm.llm_prompts import generate_story, extract_scenes
from image_audio_generator import generate_all_assets
from merge_videos import merge_all_scenes

final_prompt = "A warrior dragon"
story = generate_story(final_prompt)
scene_prompts = extract_scenes(story)

generate_all_assets(scene_prompts)
merge_all_scenes("final_story_video.mp4")
