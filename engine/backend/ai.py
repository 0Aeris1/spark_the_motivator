import os
from openai import OpenAI

class AIClient:

    def __init__(self):
        self.client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

    def generate(self, prompt: str, instructions: str) -> str:
    # Calling OpenAI API
        response = self.client.responses.create(
            model="gpt-5.2",
            instructions= instructions,
            input=prompt,
            max_output_tokens=150
        )
        return response.output_text.strip()

ai_client = AIClient()

def generate_motivation(user_text: str | None = None) -> str:
  
    instructions = ("You are motivational assistant\n"
                  "Give a short motivational and exciting message to\n"
                  "keep the user motivated and happy\n"
                  "Rules:\n"
                  "- Maximum 12 words.\n"
                  "- One sentence only.\n"
                  "- Strong and direct.\n"
                  "- No emojis.\n\n")


    prompt = user_text or "Motivate me"

    return ai_client.generate(prompt=prompt, instructions=instructions)
