import os
from dotenv import load_dotenv
import requests
load_dotenv()

from google.api_core.exceptions import (
    ResourceExhausted,      # 429 - rate limit / quota
    ServiceUnavailable,     # 503
    InternalServerError,    # 500
    Aborted,                # transient conflict, safe to retry
    DeadlineExceeded,       # timeout
)

# --- API Keys ---
GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")
YOUTUBE_API_KEY = os.environ.get("YOUTUBE_API_KEY")

# ---YOUTUBE API parameters---
GOOGLE_URL = "https://www.googleapis.com/youtube/v3/search"
PART = "snippet"
MAX_RESULTS = 5


# --- Model ---
DEFAULT_MODEL = "models/gemini-3.1-flash-lite"
TEMPERATURE = 0.5
MAX_RETRIES = 0

# --- Token limits ---
INPUT_TOKEN_LIMIT = {
    "models/gemini-3.1-flash-lite": 1048576,
}

OUTPUT_TOKEN_LIMIT = {
    "models/gemini-3.1-flash-lite": 65536,
}

# --- Pricing ---
PRICING = {
    "models/gemini-3.1-flash-lite": {
        "input_cost_per_1M_tokens": 0.25,
        "output_cost_per_1M_tokens": 1.5,
    },
}

# --- Retry: LLM ---
MAX_RETRIES_LLM = 3
BASE_DELAY_LLM = 2.0
MAX_DELAY_LLM = 30.0

GEMINI_RETRYABLE = (
    ResourceExhausted,
    ServiceUnavailable,
    InternalServerError,
    Aborted,
    DeadlineExceeded,
)

# --- Retry: YouTube API ---
MAX_RETRIES_YOUTUBE = 3
BASE_DELAY_YOUTUBE = 1.0
MAX_DELAY_YOUTUBE = 10.0
RETRYABLE_CODES = (429, 500, 502, 503, 504)

class RetryableAPIError(Exception):
    pass

YOUTUBE_RETRYABLE = (requests.exceptions.Timeout, requests.exceptions.ConnectionError, RetryableAPIError)

# --- Retry: Transcript ---
MAX_RETRIES_TRANSCRIPT = 3 
BASE_DELAY_TRANSCRIPT = 1.0
MAX_DELAY_TRANSCRIPT = 10.0

TRANSCRIPT_RETRYABLE = (
    requests.exceptions.Timeout,
    requests.exceptions.ConnectionError,
)

