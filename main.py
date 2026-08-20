from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from openai import OpenAI
from dotenv import load_dotenv
from fastapi.responses import FileResponse
from fastapi import HTTPException

app = FastAPI()
load_dotenv(override=True)
client = OpenAI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
class PitchRequest(BaseModel):
    company_name: str
    product: str
    target_audience: str
    key_message: str

@app.get("/")
def home():
    return FileResponse("index.html")
@app.post("/generate-pitch")
def generate_pitch(data: PitchRequest):

    prompt = f"""
You are a professional PR outreach assistant.

Write a short, professional and persuasive PR pitch email.

Company: {data.company_name}
Product: {data.product}
Target Audience: {data.target_audience}
Key Message: {data.key_message}

Include:
- A compelling subject line
- A short introduction
- Why the product is interesting
- Why it matters to the target audience
- A polite call to action

Keep the email concise and professional.
"""

    try:
        response = client.responses.create(
            model="gpt-5.6-luna",
            input=prompt
        )

        return {
            "pitch": response.output_text,
            "mode": "ai"
        }

    except Exception:
        fallback_pitch = f"""
Subject: PR Opportunity for {data.company_name}

Hello,

I would like to introduce {data.company_name} and its {data.product}.

This solution is designed for {data.target_audience} and focuses on:

{data.key_message}

We believe this could be a relevant story for your audience and would be happy to provide more details or arrange a short conversation.

Best regards,
PR Team
"""

        return {
            "pitch": fallback_pitch,
            "mode": "fallback"
        }