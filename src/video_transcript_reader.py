from src import retry_with_backoff
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import (
    TranscriptsDisabled,
    NoTranscriptFound,
    VideoUnavailable,
)
import requests

TRANSCRIPT_RETRYABLE = (
    requests.exceptions.Timeout,
    requests.exceptions.ConnectionError,
)

@retry_with_backoff(max_retries=3, base_delay=1.0, exceptions=TRANSCRIPT_RETRYABLE)
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