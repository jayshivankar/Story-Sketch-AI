import streamlit as st
from audiorecorder import audiorecorder
import requests
from io import BytesIO

API_URL = "http://localhost:8000/transcribe"  # FastAPI backend endpoint

st.set_page_config(page_title="🎙️ StorySketch - Voice to Text", layout="centered")
st.title("🎨 StorySketch")
st.subheader("Speak or type your story prompt — Let AI write it!")

# Step 1: Optional text input
user_text = st.text_input("📝 Or type your story idea here:", placeholder="A robot finds treasure on the moon...")

# Step 2: Optional audio input
st.markdown("🎤 Or record your story prompt:")
audio = audiorecorder("Click to record", "Recording...")

transcript = None

if audio is not None:
    try:
        # Convert AudioSegment to WAV bytes
        buffer = BytesIO()
        audio.export(buffer, format="wav")
        audio_bytes = buffer.getvalue()

        # Playback recorded audio
        st.audio(audio_bytes, format="audio/wav")

        # Send to FastAPI backend for transcription
        with st.spinner("⏳ Transcribing your voice via Whisper (Groq)..."):
            response = requests.post(
                API_URL,
                files={"file": ("recording.wav", audio_bytes, "audio/wav")}
            )

            if response.status_code == 200:
                transcript = response.json()["transcript"]
                st.success("✅ Transcription successful!")
                st.markdown(f"**📜 Transcript (from audio):** {transcript}")
            else:
                st.error("❌ Transcription failed.")
                st.json(response.json())

    except Exception as e:
        st.error(f"Error handling audio: {e}")

# Step 3: Final prompt logic
final_prompt = user_text.strip() if user_text.strip() else transcript

if final_prompt:
    st.markdown("---")
    st.markdown("### ✅ Final Prompt to Use for Story Generation")
    st.markdown(f"> {final_prompt}")
    # This prompt will later go to your story generator (Groq LLaMA)
