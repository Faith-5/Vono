from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from app.task_extractor import extract_tasks
from app.service import transcribe as transcribe_service
import json
import os

app = FastAPI()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_DIR = os.path.join(BASE_DIR, "static")

app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

MAX_FILE_SIZE = 10 * 1024 * 1024
ALLOWED_TYPES = {"audio/webm", "audio/ogg", "audio/wav", "audio/mpeg", "audio/mp4"}

@app.get("/")
async def root():
    index_path = os.path.join(STATIC_DIR, "index.html")
    return FileResponse(index_path)

@app.post("/transcribe")
async def transcribe(file: UploadFile = File(...)):

    if file.content_type not in ALLOWED_TYPES:
        raise HTTPException(status_code=400, detail= f"Invalid file type: {file.content_type}")
    
    contents = await file.read()

    if len(contents) > MAX_FILE_SIZE:
        raise HTTPException(status_code=400, detail="File too large, maximum size is 10MB")
    
    if len(contents) == 0:
        raise HTTPException(status_code=400, detail="Empty file")

    try:
        transcription = await transcribe_service(filename=file.filename, file_bytes=contents)
        tasks = extract_tasks(transcription["transcription"])
        return {"transcription": transcription["transcription"], "tasks": tasks}
    
    except HTTPException:
        raise

    except Exception as e:
        raise HTTPException(status_code=500, detail= f'Error during transcription: {e}')

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)