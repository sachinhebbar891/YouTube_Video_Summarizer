from src import retry_with_backoff
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import (
    TranscriptsDisabled,
    NoTranscriptFound,
    VideoUnavailable,
)

from src.config import (
    MAX_RETRIES_TRANSCRIPT,
    BASE_DELAY_TRANSCRIPT,
    MAX_DELAY_TRANSCRIPT,
    TRANSCRIPT_RETRYABLE
)

@retry_with_backoff(max_retries=MAX_RETRIES_TRANSCRIPT, base_delay=BASE_DELAY_TRANSCRIPT, max_delay=MAX_DELAY_TRANSCRIPT, exceptions=TRANSCRIPT_RETRYABLE)
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