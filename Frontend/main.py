import streamlit as st
from audiorecorder import audiorecorder
from api import transcribe_audio

st.set_page_config(page_title="🎨 StorySketch", layout="centered")

st.title("🎨 StorySketch")
st.caption("🚀 Speak or type your story — Let AI illustrate and narrate it!")

# Step 1: Text Input
user_text = st.text_input("📝 Or type your story idea:", placeholder="A robot finds treasure on the moon...")

# Step 2: Audio Recorder
st.markdown("🎤 Or record your story prompt:")
audio = audiorecorder("Click to record", "Recording...")

# Final usable prompt (either text or voice)
final_prompt = None

if len(audio) > 0:
    st.audio(audio.tobytes(), format="audio/wav")
    with st.spinner("🧠 Transcribing your voice with Whisper (via FastAPI)..."):
        transcript, error = transcribe_audio(audio.tobytes())
        if transcript:
            st.success("✅ Transcription Complete")
            st.markdown(f"**📜 Transcript (from audio):** {transcript}")
            final_prompt = transcript
        else:
            st.error("❌ Transcription Failed")
            st.json(error)

elif user_text.strip():
    final_prompt = user_text.strip()

# Final Prompt Confirmation
if final_prompt:
    st.markdown("---")
    st.markdown("### ✅ Final Prompt to Use:")
    st.markdown(f"> {final_prompt}")

    # TODO: Add buttons to trigger image/audio/story generation later
    st.button("🧠 Generate Story (Coming Soon)")
    st.button("🎨 Generate Images (Coming Soon)")
