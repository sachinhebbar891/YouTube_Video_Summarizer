import requests
from src import retry_with_backoff
from src.exceptions import RetryableAPIError
from src.config import(
    YOUTUBE_API_KEY,
    GOOGLE_URL,
    PART,
    MAX_RESULTS,
    MAX_RETRIES_YOUTUBE,
    BASE_DELAY_YOUTUBE,
    MAX_DELAY_YOUTUBE,
    YOUTUBE_RETRYABLE,
    RETRYABLE_CODES
)

@retry_with_backoff(max_retries=MAX_RETRIES_YOUTUBE, base_delay=BASE_DELAY_YOUTUBE, max_delay=MAX_DELAY_YOUTUBE, exceptions=YOUTUBE_RETRYABLE)
def get_video_metadata_from_title(title):
    url = GOOGLE_URL
    params = {
        "q": title,
        "part": PART,
        "type": "video",
        "maxResults": MAX_RESULTS,
        "key": YOUTUBE_API_KEY,
    }
    response = requests.get(url, params=params, timeout=10)

    if response.status_code in RETRYABLE_CODES:
        raise RetryableAPIError(f"Retryable status: {response.status_code}")

    response.raise_for_status()

    items = response.json()["items"]
    video_metadata_list = []
    for item in items:
        video_metadata = {
            "video_id": item["id"]["videoId"],
            "title": item[PART]["title"],
            "channel": item[PART]["channelTitle"],
            "published_at": item[PART]["publishedAt"],
        }
        video_metadata_list.append(video_metadata)
    return video_metadata_list