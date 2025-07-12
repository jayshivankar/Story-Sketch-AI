# Frontend/main.py
import streamlit as st
from audiorecorder import audiorecorder
from audio_translation import transcribe_audio, save_text
import io

st.set_page_config(page_title="🎨 StorySketch", layout="centered")
st.title("🎨 StorySketch")
st.caption("🚀 Speak or type your story — Let AI bring it to life!")

# Step 1: User Input
user_text = st.text_input("📝 Or type your story idea:", placeholder="A panda flies to space...")
audio = audiorecorder("🎤 Click to record", "Recording...")

final_prompt = None
transcript = None
story = None

if len(audio) > 0:
    buffer = io.BytesIO()
    audio.export(buffer, format="wav")
    wav_bytes = buffer.getvalue()
    st.audio(wav_bytes, format="audio/wav")

    with st.spinner("🔊 Transcribing with Whisper..."):
        transcript = transcribe_audio(wav_bytes)
        st.success("📝 Transcription complete!")
        st.markdown(f"**Transcript:** {transcript}")
        final_prompt = transcript
        save_text("data/transcripts", transcript, "transcript")

elif user_text.strip():
    final_prompt = user_text.strip()


#
# if final_prompt:
#     if st.button("🧠 Generate Story"):
#         with st.spinner("Creating your magical story..."):
#             story = generate_story(final_prompt)
#             st.success("📖 Story generated!")
#             st.markdown("### Your Story")
#             st.markdown(story)
#             save_text("data/stories", story, "story")

