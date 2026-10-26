import os
import logging

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from openai import OpenAI, APIError

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="AI First Backend Capstone")


class ChatRequest(BaseModel):
    prompt: str = Field(min_length=1, max_length=4000)


@app.get("/")
def home():
    return {"message": "AI Backend API is running"}


@app.post("/api/chat")
def chat(request: ChatRequest):
    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        raise HTTPException(
            status_code=503,
            detail="AI service is not configured"
        )

    try:
        client = OpenAI(api_key=api_key)
        response = client.responses.create(
            model=os.getenv("OPENAI_MODEL", "gpt-4.1-mini"),
            input=request.prompt
        )

        return {
            "success": True,
            "answer": response.output_text
        }

    except APIError:
        logger.exception("LLM API request failed")
        raise HTTPException(
            status_code=502,
            detail="AI service request failed"
        )
