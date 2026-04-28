from fastapi import UploadFile, File
from app.voice import transcribe_audio

async def transcribe(filename: str, file_bytes: bytes):
    transcription = await transcribe_audio(filename=filename, file_bytes=file_bytes)

    return {"transcription": transcription}