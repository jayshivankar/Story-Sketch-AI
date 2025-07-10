# Frontend/main.py
import streamlit as st
from audiorecorder import audiorecorder
import io

from api import transcribe_audio  # ✅ uses separate request logic

st.set_page_config(page_title="🎨 StorySketch", layout="centered")
st.title("🎨 StorySketch")
st.caption("🚀 Speak or type your story — Let AI illustrate and narrate it!")

# Step 1: User inputs
user_text = st.text_input("📝 Or type your story idea:", placeholder="A robot finds treasure on the moon...")
st.markdown("🎤 Or record your story prompt:")
audio = audiorecorder("Click to record", "Recording...")

transcript = None
final_prompt = None

# Step 2: Handle audio
if len(audio) > 0:
    buffer = io.BytesIO()
    audio.export(buffer, format="wav")
    wav_bytes = buffer.getvalue()

    st.audio(wav_bytes, format="audio/wav")

    with st.spinner("⏳ Transcribing your voice with Groq Whisper..."):
        transcript, error = transcribe_audio(wav_bytes)

        if transcript:
            st.success("✅ Transcription complete!")
            st.markdown(f"**📜 Transcript (from audio):** {transcript}")
        else:
            st.error("❌ Transcription failed")
            st.json(error)

# Step 3: Determine final prompt
if user_text.strip():
    final_prompt = user_text.strip()
elif transcript:
    final_prompt = transcript


if __name__ == "__main__":
    print(final_prompt)


