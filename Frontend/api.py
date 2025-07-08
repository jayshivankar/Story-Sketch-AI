import requests

API_BASE = "http://localhost:8000"

def transcribe_audio(audio_bytes:bytes):
    try:
        response = requests.post(
            f"{API_BASE}/transcribe",
            files = {"file": ("recording.wav",audio_bytes,"audio/wav")}
        )
        if response.status_code == 200:
            return response.json()["transcript"]
        else:
            return None,response.json()
    except Exception as e:
        return None,str(e)
