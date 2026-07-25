import streamlit as st

st.set_page_config(
    page_title="Reception Voice Agent",
    page_icon="🎙️",
    layout="wide"
)

st.title("🎙️ AI Reception Voice Agent")

st.markdown("""
Welcome to the AI Reception Voice Agent.

This application can:
- 🎤 Accept a caller's voice recording
- 📝 Convert speech to text
- 🤖 Extract caller details using AI
- 💾 Store call records in a database
- 📋 Display previous call history
""")

st.divider()

audio_file = st.file_uploader(
    "Upload a voice recording",
    type=["wav", "mp3", "m4a"]
)

if audio_file:
    st.success("Voice file uploaded successfully!")
    st.audio(audio_file)