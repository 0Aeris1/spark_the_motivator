import os

from openai import OpenAI
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

class AIClient:

    def __init__(self):
        self.client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

    def generate(self, prompt: str) -> str:
    # Calling OpenAI API
        response = self.client.responses.create(
            model="gpt-5.2",
            instructions= ("You are an motivational assistant\n"
                        "Give a short motivational and exciting message to\n"
                        "keep the user motivated and happy\n"
                        "Rules:\n"
                        "- Maximum 30 words.\n"
                        "- Strong and direct.\n"
                        "- No emojis.\n\n"),
            input=prompt,
            max_output_tokens=150
        )
        return response.output_text.strip()

ai_client = AIClient()

class MotivationRequest(BaseModel):
    text: str | None = None

class MotivationResponse(BaseModel):
    response: str

def generate_motivation(user_text: str | None = None) -> str:
  

    if user_text:
        prompt = (
                    f"User's text: {user_text}\n"
                )
    else:
        prompt = ("You are motivational assistant\n"
                  "Give a short motivational and exciting message to\n"
                  "keep the user motivated and happy\n"
                  "Rules:\n"
                  "- Maximum 12 words.\n"
                  "- One sentence only.\n"
                  "- Strong and direct.\n"
                  "- No emojis.\n\n")

    return ai_client.generate(prompt)

app.add_middleware(
        CORSMiddleware,
        allow_origins = ["*"],
        allow_methods = ["*"],
        allow_headers = ["*"],
        allow_credentials = True
        )


@app.post("/motivate", response_model=MotivationResponse)
def motivate(req: MotivationRequest):
    reply = generate_motivation(req.text)

    return {"response": reply}


