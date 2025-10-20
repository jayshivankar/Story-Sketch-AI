from moviepy import VideoFileClip, concatenate_videoclips
import os

def merge_all_scenes(output_file="final_story_video.mp4"):
    video_dir = "data/videos"
    scene_files = sorted(
        [os.path.join(video_dir, f) for f in os.listdir(video_dir) if f.endswith(".mp4")]
    )

    if not scene_files:
        raise FileNotFoundError("No video scenes found in data/videos.")

    clips = [VideoFileClip(f) for f in scene_files]
    final = concatenate_videoclips(clips, method="compose")
    final.write_videofile(output_file, fps=24, codec="libx264", audio_codec="aac")
    print(f"✅ Final video created: {output_file}")

