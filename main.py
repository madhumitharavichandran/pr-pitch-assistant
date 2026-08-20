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
    tone: str

@app.get("/")
def home():
    return FileResponse("index.html")
@app.post("/generate-pitch")
def generate_pitch(data: PitchRequest):

    prompt = f"""
You are a professional PR outreach assistant.

Write a short, persuasive PR pitch email.

Company: {data.company_name}
Product: {data.product}
Target Audience: {data.target_audience}
Key Message: {data.key_message}
Tone: {data.tone}

Include:
- A compelling subject line
- A short introduction
- Why the product is interesting
- Why it matters to the target audience
- A polite call to action

Follow the requested tone.
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

        if data.tone == "friendly":
            fallback_pitch = f"""
Subject: A story your audience might love — {data.company_name}

Hi there,

I wanted to share something exciting from {data.company_name}.

Our {data.product} is designed especially for {data.target_audience}, with one simple goal:

{data.key_message}

We think this could be a great fit for your audience and would love to share more details with you.

Looking forward to hearing from you!

Best,
PR Team
"""

        elif data.tone == "bold":
            fallback_pitch = f"""
Subject: {data.company_name} is changing the way {data.target_audience} work

Hello,

Meet {data.company_name}.

Our {data.product} is built to make a real difference for {data.target_audience}.

The idea is simple:

{data.key_message}

We believe this is a story worth talking about. We'd be happy to provide more information or arrange a conversation.

Best regards,
PR Team
"""

        else:
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