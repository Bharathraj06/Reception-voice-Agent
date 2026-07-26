import streamlit as st
from voice_agent import speech_to_text
from ai_processor import extract_details
from database import save_call, get_calls


# Page configuration
st.set_page_config(
    page_title="AI Reception Voice Agent",
    page_icon="🎙️",
    layout="wide"
)


# Title
st.title("🎙️ AI Reception Voice Agent")


st.markdown("""
### Welcome to AI Reception Assistant

This AI agent can:
- 🎤 Accept caller voice recordings
- 📝 Convert speech into text
- 🤖 Understand caller requirements
- 📋 Extract caller information
- 💾 Store call records
""")


st.divider()


# Upload audio
audio_file = st.file_uploader(
    "Upload Caller Voice Recording",
    type=["wav", "mp3", "m4a"]
    
    
)


if audio_file:

    st.success("Audio uploaded successfully!")

    st.audio(audio_file)


    if st.button("🚀 Process Call"):

        # Speech to Text
        with st.spinner("Converting voice to text..."):

            transcript = speech_to_text(audio_file)


        st.subheader("📝 Call Transcript")

        st.write(transcript)


        # AI Analysis
        with st.spinner("AI analyzing caller details..."):

            details = extract_details(transcript)


        st.subheader("🤖 AI Extracted Caller Information")

        st.info(details)


        # Save to MongoDB
        with st.spinner("Saving call record..."):

            save_call(
                transcript,
                details
            )


        st.success("Call saved to database!")

        st.success("Call processed successfully!")
        
        
        st.divider()

st.subheader("📋 Previous Call History")


if st.button("View Call History"):

    calls = get_calls()

    if calls:

        for call in calls:

            st.write("--------------------")

            st.write("📅 Time:")
            st.write(call["time"])

            st.write("📝 Transcript:")
            st.write(call["transcript"])

            st.write("🤖 Caller Details:")
            st.write(call["caller_details"])

    else:

        st.info("No call records found.")