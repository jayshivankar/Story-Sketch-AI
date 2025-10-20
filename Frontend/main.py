import streamlit as st
from audio_recorder_streamlit import audio_recorder
from audio_translation import transcribe_audio, save_text
import sys
import os
import io

# Add root path for relative module resolution
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from llm.llm_prompts import generate_story, extract_scenes
from image_audio_generator import generate_all_assets
from merge_videos import merge_all_scenes

# Streamlit page config
st.set_page_config(page_title="🎨 StorySketch", layout="centered")
st.markdown("<h1 style='text-align: center;'>🎨 StorySketch</h1>", unsafe_allow_html=True)
st.caption("🚀 Speak or type your story — Let AI bring it to life!")
st.markdown("---")

# Step 1: User Input
st.subheader("🎤 Voice or ✍️ Text Prompt")
col1, col2 = st.columns(2)

# Text Input
with col1:
    user_text = st.text_input("📝 Type your story idea", placeholder="A panda flies to space...")

# Audio Input
with col2:
    audio = audio_recorder("🎙️ Record Prompt","Recording...")

final_prompt = None
transcript = None

# Process audio input
if audio:
    buffer = io.BytesIO()
    audio.export(buffer, format="wav")
    wav_bytes = buffer.getvalue()
    st.audio(wav_bytes, format="audio/wav")

    with st.spinner("🔊 Transcribing..."):
        try:
            transcript = transcribe_audio(wav_bytes)
            st.success("📝 Transcription complete!")
            st.markdown(f"**Transcript:** `{transcript}`")
            final_prompt = transcript
            save_text("data/transcripts", transcript, "transcript")
        except Exception as e:
            st.error(f"Error during transcription: {e}")

# Use text input if available
elif user_text.strip():
    final_prompt = user_text.strip()

# Main generation logic
if final_prompt:
    st.markdown("---")
    st.button("✨ Generate Story & Video")  # Change to button widget

    with st.spinner("🧠 Generating story..."):
        try:
            story = generate_story(final_prompt)
            st.success("📖 Story generated!")
            st.markdown("### 📚 Story:")
            st.markdown(story)
        except Exception as e:
            st.error(f"Error during story generation: {e}")

    if story:
        with st.spinner("🪄 Extracting scene prompts..."):
            try:
                scenes = extract_scenes(story)
                st.success(f"📸 Extracted {len(scenes)} scenes!")
            except Exception as e:
                st.error(f"Error extracting scenes: {e}")

        if scenes:
            with st.spinner("🎨 Generating images and audio..."):
                try:
                    generate_all_assets(scenes)
                except Exception as e:
                    st.error(f"Error during asset generation: {e}")

            with st.spinner("🎬 Merging scene videos..."):
                try:
                    output_path = "final_story_video.mp4"
                    merge_all_scenes(output_path)
                    st.success("✅ Final video is ready!")
                    st.video(output_path)
                except Exception as e:
                    st.error(f"Error during video merging: {e}")
else:
    st.info("💡 Please enter text or record audio to start.")

