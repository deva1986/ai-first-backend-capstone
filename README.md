# AI First Backend Capstone

## Project Overview

AI First Backend Capstone is an AI-powered web application that allows users to submit prompts through a frontend interface and receive AI-generated responses.

The application uses a Laravel backend API to validate requests, communicate with a Large Language Model (LLM) API, and return responses to the frontend.

## Technology Stack

- **Backend:** PHP, Laravel
- **Frontend:** HTML, CSS, JavaScript (or React)
- **AI Integration:** LLM API
- **API Format:** REST API with JSON
- **Version Control:** Git and GitHub
- **Deployment Target:** AWS

## Application Architecture

User → Frontend → Laravel Backend API → LLM API → Laravel Backend → Frontend

The frontend communicates with the Laravel backend through a REST API. The backend validates user input, securely calls the LLM API, handles errors, and returns the generated response.

## Features

- AI-powered question-and-answer functionality
- REST API integration
- Request validation
- JSON request and response handling
- Error handling for failed LLM API requests
- Secure API key management using environment variables
- Separation of frontend and backend responsibilities

## API Endpoint

**POST `/api/chat`**

### Example Request

```json
{
  "prompt": "What is Laravel?"
}
```

### Example Success Response

```json
{
  "success": true,
  "answer": "Laravel is a PHP web application framework."
}
```

### Example Error Response

```json
{
  "success": false,
  "message": "The AI service is temporarily unavailable."
}
```

The exact HTTP status code and response structure should be implemented consistently in the backend.

## Setup Instructions

### Prerequisites

- PHP version supported by the Laravel version used
- Composer
- Node.js and npm if using a frontend build tool
- An API key from your chosen LLM provider

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/deva1986/ai-first-backend-capstone.git
   cd ai-first-backend-capstone
   ```

2. Install PHP dependencies:

   ```bash
   composer install
   ```

3. Create your environment file:

   ```bash
   cp .env.example .env
   ```

4. Generate the Laravel application key:

   ```bash
   php artisan key:generate
   ```

5. Configure your LLM provider credentials in `.env`, using the environment variable names expected by your implementation.

6. Start the Laravel development server:

   ```bash
   php artisan serve
   ```

7. Open the application at `http://127.0.0.1:8000`.

**Note:** These instructions assume the repository contains a Laravel application with a valid `composer.json`, `.env.example`, and the required routes and controllers. These files must be implemented before the application can run.

## Security

- Store API keys in environment variables.
- Never commit `.env` or other secret files to GitHub.
- Validate and limit user input.
- Handle API timeouts and provider errors gracefully.
- Avoid exposing internal exception details to clients.
- Configure rate limiting to help prevent API abuse.

## Testing

The application should be tested for:

- Valid prompts and successful AI responses
- Empty or invalid prompts
- Prompts exceeding the allowed length
- Missing or invalid LLM API credentials
- LLM API failures and timeouts
- Appropriate HTTP status codes and JSON responses

## Deployment

The application is intended to be deployable on AWS. Potential deployment components include:

- Amazon EC2 or another suitable compute service
- Nginx as a web server
- PHP-FPM for Laravel
- Environment-based secret configuration
- HTTPS and appropriate access controls

AWS deployment configuration will be added as the project progresses.

## Project Status

**Initial project setup — implementation in progress.**

The Laravel application, frontend, LLM integration, automated tests, and deployment configuration must be completed and verified.

## Author

GitHub: [deva1986](https://github.com/deva1986)

## Assignment

Scaler — Backend Projects: Deploying Backend & AI-Enabled Applications to AWS.
