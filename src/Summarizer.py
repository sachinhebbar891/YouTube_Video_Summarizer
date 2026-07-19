from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-pro",
    google_api_key=os.environ["GOOGLE_API_KEY"],
    temperature = 0.5
)

def summarize(transcript: str, summary_type: str) -> str:
    prompt = f"""
    
    Summarize the following video transcript.
    Focus specifically on: {summary_type}

    Transcript:
    {transcript}
    
    """
    response = llm.invoke(prompt)
    return response.content