from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
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
    return {"message": "PR Pitch Assistant is running"}

@app.post("/generate-pitch")
def generate_pitch(data: PitchRequest):

    pitch = f"""
Subject: PR Opportunity for {data.company_name}

Hello,

I would like to introduce {data.company_name} and its {data.product}.

Our target audience is {data.target_audience}, and the key message we want to communicate is:

{data.key_message}

We believe this story could be relevant and valuable for your audience.

Best regards,
PR Team
"""

    return {"pitch": pitch}