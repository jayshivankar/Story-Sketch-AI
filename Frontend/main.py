import streamlit as st
from audiorecorder import audiorecorder
import requests

API_URL = "http://localhost:8000/transcribe"  # FastAPI backend

st.set_page_config(page_title="🎙️ StorySketch - Voice to Text", layout="centered")
st.title("🎨 StorySketch")
st.subheader("Speak or type your story prompt — Let AI write it!")

# Step 1: Text Input (optional)
user_text = st.text_input("📝 Or type your story idea here:", placeholder="A panda builds a spaceship...")

# Step 2: Record audio (optional)
st.markdown("🎤 Or record your story prompt:")
audio = audiorecorder("Click to record", "Recording...")

transcript = None

# Handle transcription if audio is recorded
if len(audio) > 0:
    st.audio(audio.tobytes(), format="audio/wav")

    with st.spinner("⏳ Transcribing your voice using Whisper via FastAPI..."):
        response = requests.post(
            API_URL,
            files={"file": ("recording.wav", audio.tobytes(), "audio/wav")}
        )

        if response.status_code == 200:
            transcript = response.json()["transcript"]
            st.success("✅ Transcription Successful!")
            st.markdown(f"**📜 Transcript (from audio):** {transcript}")
        else:
            st.error("❌ Transcription Failed")
            st.json(response.json())

# Final text input (either manual or from audio)
final_prompt = user_text.strip() if user_text.strip() else transcript

if final_prompt:
    st.markdown("---")
    st.markdown(f"### ✅ Final Prompt to Use")
    st.markdown(f"> {final_prompt}")
    # Later you can send `final_prompt` to Groq LLaMA for story generation
