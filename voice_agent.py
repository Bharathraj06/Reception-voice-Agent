from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def speech_to_text(audio_file):

    audio_file.seek(0)

    response = client.audio.transcriptions.create(
        model="whisper-large-v3",
        file=audio_file
    )

    return response.text