# Meeting Summarizer

Automatically transcribe meeting audio and generate concise summaries with action items to save time and boost productivity.

---

## Features
- Convert meeting audio (MP3/WAV) to text using ASR (OpenAI Whisper, Google Speech-to-Text)
- Generate concise summaries with key decisions and action items
- Optional frontend to upload audio and view results
- Store transcripts and summaries for future reference

---

## Tech Stack
- **Backend:** Python, FastAPI  
- **ASR:** Whisper / Google Speech-to-Text  
- **Summarization:** OpenAI GPT / LLMs  
- **Frontend (Optional):** React / Streamlit  
- **Storage:** Local JSON / Database  

---

## Installation
```bash
git clone https://github.com/yourusername/meeting-summarizer.git
cd meeting-summarizer/backend
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
pip install -r requirements.txt
