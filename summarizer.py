import openai

def generate_summary(transcript):
    prompt = f'''
    Summarize this meeting transcript into:
    - Key Points
    - Decisions Made
    - Action Items

    Transcript:
    {transcript}
    '''
    response = openai.Chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content
