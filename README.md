
# AI First Backend Capstone

An AI-powered web application built with Python FastAPI, HTML, CSS,
JavaScript, and the OpenAI API.

## Architecture

User -> Frontend -> FastAPI Backend -> OpenAI API
     -> FastAPI Backend -> Frontend

The frontend and backend are separate components.
The frontend sends JSON requests to the backend REST API.
The backend validates input, calls the LLM API, and returns JSON.

## Technology Stack

- Backend: Python and FastAPI
- Frontend: HTML, CSS, JavaScript
- AI integration: OpenAI API
- Validation: Pydantic
- API documentation: OpenAPI / Swagger UI
- Version control: Git and GitHub

## Features

- AI-powered question and answer
- REST API with JSON request and response
- Input validation
- Error handling for missing credentials and API failures
- Configurable AI model
- Health check endpoint
- Frontend and backend separation

## API Endpoints

### GET /

Serves the frontend application.

### GET /health

Example response:

{
  "status": "ok"
}

### POST /api/chat

Example request:

{
  "prompt": "What is FastAPI?"
}

Example successful response:

{
  "success": true,
  "answer": "FastAPI is a Python web framework."
}

Possible errors include:
- 422: Invalid request
- 502: AI provider request failed
- 503: AI service is not configured

## Prerequisites

- Python 3.10 or a compatible newer version
- pip
- An OpenAI API key with API access and available quota

## Installation

Clone the repository:

    git clone https://github.com/deva1986/ai-first-backend-capstone.git
    cd ai-first-backend-capstone

Create a virtual environment:

    python -m venv .venv

Activate it on Windows:

    .venv\Scripts\activate

Activate it on macOS or Linux:

    source .venv/bin/activate

Install dependencies:

    pip install -r requirements.txt

## Configuration

Set the API key as an environment variable.

Windows PowerShell:

    $env:OPENAI_API_KEY="your-api-key"

macOS or Linux:

    export OPENAI_API_KEY="your-api-key"

Optionally configure the model:

    OPENAI_MODEL=gpt-4.1-mini

Never commit API keys or other secrets to GitHub.

## Run the Application

Start the server:

    uvicorn app:app --reload

Open the application:

    http://127.0.0.1:8000

Interactive API documentation:

    http://127.0.0.1:8000/docs

Health check:

    http://127.0.0.1:8000/health

## Testing the API

Example curl request:

    curl -X POST http://127.0.0.1:8000/api/chat \
      -H "Content-Type: application/json" \
      -d '{"prompt":"Explain REST APIs"}'

## Security

- Store API keys in environment variables.
- Never commit secrets to source control.
- Validate and limit user input.
- Handle provider failures without exposing sensitive details.
- Use HTTPS and rate limiting in production.

## Deployment

The application can be deployed to AWS after testing and configuration.
A production deployment should include secret management, HTTPS,
monitoring, and suitable access controls.

## Project Status

Initial implementation. Run and test the application locally before
considering it production-ready.

## Author

GitHub: https://github.com/deva1986

## Assignment

Scaler - Backend Projects: Deploying Backend & AI-Enabled Applications
to AWS.
