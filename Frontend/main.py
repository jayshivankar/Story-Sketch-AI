import streamlit as st
from audiorecorder import audiorecorder
from audio_translation import transcribe_audio, save_text
from Llm.llm_prompts import generate_story, extract_scenes
from image_audio_generator import generate_all_assets
from merge_videos import merge_all_scenes
import io
import os

st.set_page_config(page_title="🎨 StorySketch", layout="centered")
st.markdown("<h1 style='text-align: center;'>🎨 StorySketch</h1>", unsafe_allow_html=True)
st.caption("🚀 Speak or type your story — Let AI bring it to life!")
st.markdown("---")

# Step 1: User Input
st.subheader("🎤 Voice or ✍️ Text Prompt")
col1, col2 = st.columns(2)

with col1:
    user_text = st.text_input("📝 Type your story idea", placeholder="A panda flies to space...")

with col2:
    audio = audiorecorder("🎙️ Record Prompt", "Recording...")

final_prompt = None
transcript = None

# Process audio input
if len(audio) > 0:
    buffer = io.BytesIO()
    audio.export(buffer, format="wav")
    wav_bytes = buffer.getvalue()
    st.audio(wav_bytes, format="audio/wav")

    with st.spinner("🔊 Transcribing..."):
        transcript = transcribe_audio(wav_bytes)
        st.success("📝 Transcription complete!")
        st.markdown(f"**Transcript:** `{transcript}`")
        final_prompt = transcript
        save_text("data/transcripts", transcript, "transcript")

elif user_text.strip():
    final_prompt = user_text.strip()

st.markdown("---")

# Main generation logic
if final_prompt:
    if st.button("✨ Generate Story & Video"):
        with st.spinner("🧠 Generating story..."):
            story = generate_story(final_prompt)
            st.success("📖 Story generated!")
            st.markdown("### 📚 Story:")
            st.markdown(story)

        with st.spinner("🪄 Extracting scene prompts..."):
            scenes = extract_scenes(story)
            st.success(f"📸 Extracted {len(scenes)} scenes!")

        with st.spinner("🎨 Generating images and audio..."):
            generate_all_assets(scenes)

        with st.spinner("🎬 Merging scene videos..."):
            output_path = "final_story_video.mp4"
            merge_all_scenes(output_path)

        st.success("✅ Final video is ready!")
        st.video(output_path)

else:
    st.info("💡 Please enter text or record audio to start.")
