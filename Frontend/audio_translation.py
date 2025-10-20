import os
import io
from datetime import datetime
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

groq_client = Groq(api_key=GROQ_API_KEY)

def transcribe_audio(audio_bytes: bytes) -> str:
    """Transcribe audio to text using Groq Whisper."""
    if not audio_bytes:
        raise ValueError("Empty audio input detected.")

    try:
        buffer = io.BytesIO(audio_bytes)
        buffer.name = "recording.wav"

        result = groq_client.audio.transcriptions.create(
            file=buffer,
            model="whisper-large-v3-turbo",
            language="en",
            response_format="json"
        )
        return result.text.strip()

    except Exception as e:
        raise RuntimeError(f"Groq transcription failed: {e}")

def save_text(folder: str, content: str, prefix: str) -> str:
    """Save text content with timestamp."""
    os.makedirs(folder, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{prefix}_{timestamp}.txt"
    path = os.path.join(folder, filename)

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    return path
