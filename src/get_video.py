from googleapiclient.discovery import build

from dotenv import load_dotenv
import os

load_dotenv()

youtube_api_key = os.getenv("YOUTUBE_API_KEY")

youtube = build("youtube", "v3", developerKey=youtube_api_key)

def get_video_metadata_from_title(title):
    request = youtube.search().list(q=title, part="snippet", type="video", maxResults=5)
    response = request.execute()
    items = response["items"]
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