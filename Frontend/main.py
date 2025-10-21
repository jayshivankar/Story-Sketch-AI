import streamlit as st
import tempfile
from Frontend.audio_translation import transcribe_audio, save_text
from llm.llm_prompts import generate_story, extract_scenes
from image_audio_generator import generate_all_assets
from merge_videos import merge_all_scenes


# ------------------------------------------------------------
# Streamlit Page Setup
# ------------------------------------------------------------
st.set_page_config(page_title="🎨 StorySketch", page_icon="🎬", layout="centered")
st.title("🎨 StorySketch – Turn Voice Into Magical Stories")
st.caption("🎙️ Speak or type your idea — Let AI create the story, images, and video!")
st.markdown("---")


# ------------------------------------------------------------
# Initialize Session State
# ------------------------------------------------------------
for key in ["final_prompt", "story", "scenes", "video_ready"]:
    if key not in st.session_state:
        st.session_state[key] = None


# ------------------------------------------------------------
# Input Section: Voice Upload or Text
# ------------------------------------------------------------
tab1, tab2 = st.tabs(["🎤 Voice Upload", "✍️ Text Input"])

with tab1:
    st.info("Upload your audio idea (WAV or MP3) to let AI transcribe it.")
    uploaded_audio = st.file_uploader("Upload your audio file", type=["wav", "mp3"])

    if uploaded_audio:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_file:
            temp_file.write(uploaded_audio.read())
            audio_path = temp_file.name

        st.audio(audio_path)
        st.success("✅ Audio file ready for transcription")

        if st.button("🧠 Transcribe Audio"):
            with st.spinner("Transcribing your audio..."):
                try:
                    text_prompt = transcribe_audio(audio_path)
                    save_text(text_prompt)
                    st.session_state["final_prompt"] = text_prompt
                    st.success("✅ Transcription complete!")
                    st.write("**Transcribed Text:**")
                    st.write(text_prompt)
                except Exception as e:
                    st.error(f"❌ Error during transcription: {e}")


with tab2:
    st.info("Type your story idea directly.")
    text_input = st.text_area("Your Story Idea")
    if st.button("💡 Save Text"):
        if text_input.strip():
            st.session_state["final_prompt"] = text_input.strip()
            st.success("✅ Text saved!")
        else:
            st.warning("Please enter some text before saving.")


# ------------------------------------------------------------
# Step 2 – Story Generation
# ------------------------------------------------------------
st.markdown("---")
st.header("🧠 Story Generation")

if st.session_state["final_prompt"]:
    if st.button("✨ Generate Story"):
        with st.spinner("Generating your story..."):
            try:
                story = generate_story(st.session_state["final_prompt"])
                st.session_state["story"] = story
                st.success("✅ Story generated successfully!")
                st.write(story)
            except Exception as e:
                st.error(f"❌ Error generating story: {e}")
else:
    st.info("Please provide a text or audio idea first.")


# ------------------------------------------------------------
# Step 3 – Extract Scenes
# ------------------------------------------------------------
st.markdown("---")
st.header("🎬 Scene Extraction")

if st.session_state["story"]:
    if st.button("🎞️ Extract Scenes"):
        with st.spinner("Extracting scenes from story..."):
            try:
                scenes = extract_scenes(st.session_state["story"])
                st.session_state["scenes"] = scenes
                st.success("✅ Scenes extracted successfully!")
                for i, scene in enumerate(scenes, start=1):
                    st.write(f"**Scene {i}:** {scene}")
            except Exception as e:
                st.error(f"❌ Error extracting scenes: {e}")
else:
    st.info("Generate a story before extracting scenes.")


# ------------------------------------------------------------
# Step 4 – Generate Assets
# ------------------------------------------------------------
st.markdown("---")
st.header("🖼️ Generate Images and Audio")

if st.session_state["scenes"]:
    if st.button("🎨 Generate Assets"):
        with st.spinner("Generating images and audio..."):
            try:
                generate_all_assets(st.session_state["scenes"])
                st.success("✅ Assets generated successfully!")
            except Exception as e:
                st.error(f"❌ Error generating assets: {e}")
else:
    st.info("Please extract scenes before generating assets.")


# ------------------------------------------------------------
# Step 5 – Merge to Final Video
# ------------------------------------------------------------
st.markdown("---")
st.header("🎥 Merge to Final Video")

if st.button("🎞️ Create Final Video"):
    with st.spinner("Merging scenes into final video..."):
        try:
            final_video_path = merge_all_scenes()
            st.session_state["video_ready"] = final_video_path
            st.success("✅ Final video ready!")
            st.video(final_video_path)
        except Exception as e:
            st.error(f"❌ Error merging video: {e}")
