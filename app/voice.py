import httpx
from fastapi import HTTPException
from app.client import client

async def transcribe_audio(filename: str, file_bytes: bytes):
    try:
        transcription = client.audio.transcriptions.create(
            file=(filename, file_bytes),
            model="whisper-large-v3",
            temperature=0,
            response_format="verbose_json",
        )

        return transcription.text
    
    except httpx.TimeoutException:
        raise HTTPException(status_code=500, detail="Transcription timed out")
    
    except httpx.NetworkError:
        raise HTTPException(status_code=500, detail="Network error")
    
    except Exception as e:
        raise HTTPException(status_code=500, detail= f'Error during transcription: {e}')