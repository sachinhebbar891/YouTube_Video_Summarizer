from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from src import retry_with_backoff
import os

load_dotenv()

from google.api_core.exceptions import (
    ResourceExhausted,      # 429 - rate limit / quota
    ServiceUnavailable,     # 503
    InternalServerError,    # 500
    Aborted,                # transient conflict, safe to retry
    DeadlineExceeded,       # timeout
)

llm = ChatGoogleGenerativeAI(
    model="models/gemini-3.1-flash-lite",
    google_api_key=os.environ["GOOGLE_API_KEY"],
    temperature = 0.5,
    max_retries = 0
)

GEMINI_RETRYABLE = (
    ResourceExhausted,
    ServiceUnavailable,
    InternalServerError,
    Aborted,
    DeadlineExceeded,
)


@retry_with_backoff(max_retries=3, base_delay=2.0, exceptions=GEMINI_RETRYABLE)
def summarize(prompt_messages: list) -> str:
    response = llm.invoke(prompt_messages)
    return response.content