
## Application Architecture

User → Frontend → Laravel Backend API → LLM API → Backend → Frontend

## API Endpoint

**POST /api/chat**

Example request:

```json
{
  "prompt": "What is Laravel?"
}
```

Example response:

```json
{
  "success": true,
  "answer": "Laravel is a PHP web application framework."
}
```

## Setup Instructions

1. Clone the GitHub repository.
2. Install PHP and Composer.
3. Install Laravel dependencies using `composer install`.
4. Copy `.env.example` to `.env`.
5. Configure the LLM API key in `.env`.
6. Generate the Laravel application key.
7. Start the Laravel development server.
8. Open the application in a browser.

## Security

- Store API keys in environment variables.
- Validate user input.
- Handle API failures gracefully.
- Never commit `.env` or other secrets to GitHub.

## Project Status

Initial project setup. Application implementation is pending.

## Author

GitHub: deva1986

## Assignment

Scaler – Backend Projects: Deploying Backend & AI-Enabled Applications to AWS.
