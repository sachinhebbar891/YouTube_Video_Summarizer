from googleapiclient.discovery import build
import requests
from dotenv import load_dotenv
import os

load_dotenv()

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