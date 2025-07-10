# Backend/transcribe_groq.py
import tempfile
import os
from datetime import datetime
from groq import Groq
import json

# Ensure directory exists
os.makedirs("data/transcripts", exist_ok=True)

# Load API key securely (optional if set as ENV var)
API_KEY = os.getenv("GROQ_API_KEY")

# Initialize Groq client
client = Groq(api_key=API_KEY)

def transcribe_audio(audio_bytes: bytes, api_key: str) -> str:
    # Save audio bytes to temp file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as f:
        f.write(audio_bytes)
        audio_path = f.name

    try:
        # Open and send file to Groq's Whisper transcription API
        with open(audio_path, "rb") as audio_file:
            transcription = client.audio.transcriptions.create(
                file=audio_file,
                model="whisper-large-v3",
                response_format="json",
                language="en"
            )

        # Extract text
        transcript_text = transcription.text

        # Save to file
        filename = datetime.now().strftime("transcript_%Y%m%d_%H%M%S.txt")
        save_path = os.path.join("data", "transcripts", filename)

        with open(save_path, "w", encoding="utf-8") as f:
            f.write(transcript_text)

        return transcript_text

    except Exception as e:
        return f"Error: {str(e)}"
