from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatOpenAI(
    model="gpt-5-nano",
    openai_api_key=os.environ["OPENAI_API_KEY"],
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