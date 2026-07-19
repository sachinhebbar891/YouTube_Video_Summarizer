from langchain_google_genai import ChatGoogleGenerativeAI
from src import retry_with_backoff

from src.config import (
    DEFAULT_MODEL,
    GOOGLE_API_KEY,
    TEMPERATURE,
    LANGCHAIN_INTERNAL_MAX_RETRIES,
    MAX_RETRIES_LLM,
    BASE_DELAY_LLM,
    MAX_DELAY_LLM,
    GEMINI_RETRYABLE
)

llm = ChatGoogleGenerativeAI(
    model=DEFAULT_MODEL,
    google_api_key=GOOGLE_API_KEY,
    temperature = TEMPERATURE,
    max_retries = LANGCHAIN_INTERNAL_MAX_RETRIES
)


@retry_with_backoff(max_retries=MAX_RETRIES_LLM, base_delay=BASE_DELAY_LLM, max_delay=MAX_DELAY_LLM, exceptions=GEMINI_RETRYABLE)
def summarize(prompt_messages: list) -> str:
    response = llm.invoke(prompt_messages)
    return response.content