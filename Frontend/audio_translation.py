import os
from datetime import datetime
from dotenv import load_dotenv
from groq import Groq
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage
import io

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Initialize Groq clients
groq_client = Groq(api_key=GROQ_API_KEY)


def transcribe_audio(audio_bytes: bytes) -> str:
    # Wrap in file-like object
    buffer = io.BytesIO(audio_bytes)

    # Give it a name ending in ".wav"
    buffer.name = "recording.wav"

    result = groq_client.audio.transcriptions.create(
        file=buffer,
        model="whisper-large-v3-turbo",
        language="en",
        response_format="json"
    )

    return result.text.strip()


def save_text(folder: str, content: str, prefix: str) -> str:
    os.makedirs(folder, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{prefix}_{timestamp}.txt"
    path = os.path.join(folder, filename)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    return path