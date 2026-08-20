# 🚀 PR Pitch Assistant

PR Pitch Assistant is a web application that helps users generate clear and professional PR outreach pitches from a simple company brief.

The application collects information about a company, product or service, target audience, and key message, then creates a structured PR pitch that can be used for outreach.

## ✨ Features

- Generate professional PR pitch emails
- Simple and modern user interface
- Company, product, audience, and key-message inputs
- AI integration using the OpenAI API
- Automatic fallback pitch generation when the external AI service is unavailable
- Copy generated pitches easily
- FastAPI backend
- Responsive frontend design
- Secure API key handling using environment variables

## 🛠️ Tech Stack

**Frontend**
- HTML
- CSS
- JavaScript

**Backend**
- Python
- FastAPI
- Pydantic

**AI Integration**
- OpenAI API

**Development Tools**
- Git
- GitHub
- VS Code

## ⚙️ How It Works

1. The user enters the company name.
2. The user describes the product or service.
3. The user specifies the target audience.
4. The user provides the key PR message.
5. The frontend sends the information to the FastAPI backend.
6. The backend attempts to generate the pitch using the AI service.
7. If the external AI service is unavailable, the application generates a fallback pitch.
8. The completed PR pitch is displayed in the interface.

## 📁 Project Structure

```text
pr-pitch-assistant/
│
├── main.py
├── index.html
├── .gitignore
├── README.md
└── .env        # Local only — not committed to GitHub