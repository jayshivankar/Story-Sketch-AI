# Backend/transcribe_groq.py
import tempfile
import requests
import os
from datetime import datetime

os.makedirs("data/transcripts", exist_ok=True)

def transcribe_audio(audio_bytes: bytes, api_key: str) -> str:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as f:
        f.write(audio_bytes)
        audio_path = f.name

    headers = {"Authorization": f"Bearer {api_key}"}
    files = {"file": open(audio_path, "rb")}
    data = {
        "model": "whisper-large-v2",
        "language": "en",
        "response_format": "json"
    }

    response = requests.post("https://api.groq.com/v1/audio/transcriptions",
                             headers=headers, files=files, data=data)

    if response.status_code == 200:
        transcript = response.json()["text"]
        filename = datetime.now().strftime("transcript_%Y%m%d_%H%M%S.txt")
        with open(f"data/transcripts/{filename}", "w", encoding="utf-8") as f:
            f.write(transcript)
        return transcript
    else:
        return f"Error {response.status_code}: {response.text}"
