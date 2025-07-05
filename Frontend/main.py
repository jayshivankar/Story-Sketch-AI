import streamlit as st



title = st.title("Story Sketch")

st.text_input("Give Input","Enter the start")
audio_value = st.audio_input("Record the start of any story")

if audio_value:
    st.audio(audio_value)


# button
st.button("build Story", type="primary")
