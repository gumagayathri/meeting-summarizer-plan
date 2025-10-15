from fastapi import FastAPI, UploadFile
from utils.asr_service import transcribe_audio
from utils.summarizer import generate_summary
import tempfile

app = FastAPI()

@app.post("/summarize_meeting")
async def summarize_meeting(file: UploadFile):
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp.write(await file.read())
        path = tmp.name
    transcript = transcribe_audio(path)
    summary = generate_summary(transcript)
    return {"transcript": transcript, "summary": summary}
