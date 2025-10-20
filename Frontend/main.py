import streamlit as st
from audio_recorder_streamlit import audio_recorder
from audio_translation import transcribe_audio, save_text
from llm.llm_prompts import generate_story, extract_scenes
from image_audio_generator import generate_all_assets
from merge_videos import merge_all_scenes
import io
import os

# -------------------------------
# Streamlit Page Setup
# -------------------------------
st.set_page_config(page_title="🎨 StorySketch", page_icon="🎬", layout="centered")
st.title("🎨 StorySketch – Turn Voice Into Magical Stories")
st.caption("🎙️ Speak or type your idea — Let AI create the story, images, and video!")
st.markdown("---")

# -------------------------------
# Initialize Session State
# -------------------------------
for key in ["final_prompt", "story", "scenes", "video_ready"]:
    if key not in st.session_state:
        st.session_state[key] = None

# -------------------------------
# Input Section: Voice or Text
# -------------------------------
tab1, tab2 = st.tabs(["🎤 Voice Input", "✍️ Text Input"])

with tab1:
    st.info("Record your story idea in English and let AI transcribe it.")
    audio_bytes = audio_recorder(text="Click to Record", recording_color="#ff4b4b")

    if audio_bytes:
        st.audio(audio_bytes, format="audio/wav")
        with st.spinner("Transcribing your voice... ⏳"):
            try:
                transcript = transcribe_audio(audio_bytes)
                st.session_state.final_prompt = transcript
                st.success("📝 Transcription complete!")
                st.text_area("Transcript:", transcript, height=120)
                save_text("data/transcripts", transcript, "transcript")
            except Exception as e:
                st.error(f"⚠️ Audio transcription failed: {e}")
                st.session_state.final_prompt = None

with tab2:
    text_input = st.text_area("Enter your story idea below:", placeholder="A panda learns to fly in space 🚀")
    if text_input.strip():
        st.session_state.final_prompt = text_input.strip()

# -------------------------------
# Story Generation Button
# -------------------------------
st.markdown("---")
if st.button("✨ Generate Story"):
    if not st.session_state.final_prompt:
        st.warning("⚠️ Please provide an idea using voice or text.")
    else:
        with st.spinner("🧠 Crafting your story..."):
            try:
                story = generate_story(st.session_state.final_prompt)
                st.session_state.story = story
                st.success("📖 Story generated successfully!")
                st.markdown("### 📚 Story Preview")
                st.write(story)
            except Exception as e:
                st.error(f"❌ Story generation failed: {e}")

# -------------------------------
# Scene Extraction + Video Creation
# -------------------------------
if st.session_state.story:
    with st.expander("🎬 Create Story Video", expanded=True):
        if st.button("Generate Scenes & Video"):
            try:
                with st.spinner("🪄 Extracting key scenes..."):
                    scenes = extract_scenes(st.session_state.story)
                    st.session_state.scenes = scenes
                    st.success(f"✅ Extracted {len(scenes)} scenes!")

                with st.spinner("🎨 Generating visuals and narration..."):
                    generate_all_assets(scenes)
                    st.info("Scene assets generated successfully.")

                with st.spinner("🎞️ Merging scenes into final video..."):
                    output_path = "final_story_video.mp4"
                    merge_all_scenes(output_path)
                    st.session_state.video_ready = output_path
                    st.success("🎉 Final video created successfully!")

            except Exception as e:
                st.error(f"❌ Error while generating video: {e}")

# -------------------------------
# Display Final Video
# -------------------------------
if st.session_state.video_ready:
    st.markdown("### 🎥 Your Final Story Video")
    st.video(st.session_state.video_ready)
    with open(st.session_state.video_ready, "rb") as f:
        st.download_button("⬇️ Download Video", f, file_name="final_story_video.mp4")

st.markdown("---")
st.caption("🚀 Built using Streamlit, Groq LLM, Replicate, and gTTS.")
