from googleapiclient.discovery import build
from src import retry_with_backoff
import requests
from dotenv import load_dotenv
import os

class RetryableAPIError(Exception):
    pass

load_dotenv()

@retry_with_backoff(max_retries=3, base_delay=1.0, exceptions=(requests.exceptions.Timeout, requests.exceptions.ConnectionError, RetryableAPIError))
def get_video_metadata_from_title(title, max_results=5):
    url = "https://www.googleapis.com/youtube/v3/search"
    params = {
        "q": title,
        "part": "snippet",
        "type": "video",
        "maxResults": max_results,
        "key": os.getenv("YOUTUBE_API_KEY"),
    }
    response = requests.get(url, params=params, timeout=10)

    if response.status_code in (429, 500, 502, 503, 504):
        raise RetryableAPIError(f"Retryable status: {response.status_code}")

    response.raise_for_status()

    items = response.json()["items"]
    video_metadata_list = []
    for item in items:
        video_metadata = {
            "video_id": item["id"]["videoId"],
            "title": item["snippet"]["title"],
            "channel": item["snippet"]["channelTitle"],
            "published_at": item["snippet"]["publishedAt"],
        }
        video_metadata_list.append(video_metadata)
    return video_metadata_list