
import logging
import os
from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from openai import APIError, OpenAI
from pydantic import BaseModel, Field

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="AI First Backend Capstone",
    description="AI-powered question and answer API",
    version="1.0.0",
)

BASE_DIR = Path(__file__).resolve().parent
FRONTEND_FILE = BASE_DIR / "frontend" / "index.html"


class ChatRequest(BaseModel):
    prompt: str = Field(
        min_length=1,
        max_length=4000,
        description="Question or prompt for the AI",
    )


@app.get("/")
def home():
    """Serve the frontend application."""
    if not FRONTEND_FILE.is_file():
        raise HTTPException(
            status_code=500,
            detail="Frontend file not found",
        )

    return FileResponse(FRONTEND_FILE)


@app.get("/health")
def health():
    """Health check endpoint."""
    return {"status": "ok"}


@app.post("/api/chat")
def chat(request: ChatRequest):
    """Validate the prompt and request an AI-generated response."""
    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        raise HTTPException(
            status_code=503,
            detail="AI service is not configured",
        )

    try:
        client = OpenAI(
            api_key=api_key,
            timeout=30.0,
            max_retries=1,
        )

        response = client.responses.create(
            model=os.getenv("OPENAI_MODEL", "gpt-4.1-mini"),
            input=request.prompt,
        )

        answer = response.output_text

        return {
            "success": True,
            "answer": answer,
        }

    except APIError:
        logger.exception("LLM API request failed")

        raise HTTPException(
            status_code=502,
            detail="AI service request failed",
        )
