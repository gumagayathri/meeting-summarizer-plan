import openai

def transcribe_audio(file_path):
    with open(file_path, "rb") as f:
        result = openai.Audio.transcriptions.create(
            model="whisper-1", file=f
        )
    return result.text
