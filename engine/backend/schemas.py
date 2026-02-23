from pydantic import BaseModel

class MotivationRequest(BaseModel):
    text: str | None = None

class MotivationResponse(BaseModel):
    response: str
