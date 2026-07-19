from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="models/gemini-3.1-flash-lite",
    google_api_key=os.environ["GOOGLE_API_KEY"],
    temperature = 0.5
)

def summarize(prompt_messages: list) -> str:
    response = llm.invoke(prompt_messages)
    return response.content