from youtube_transcript_api import YouTubeTranscriptApi

def get_transcript(video_id):
    api = YouTubeTranscriptApi()
    try:
        transcript = api.fetch(video_id)
        return transcript
    except Exception as e:
        print(f"Error fetching transcript: {e}")
        return None
    
def format_transcript(transcript):
    formatted_transcript = ""
    for entry in transcript:
        formatted_transcript += f"{entry.text} "
    return formatted_transcript.strip()