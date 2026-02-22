from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

class MotivationRequest(BaseModel):
    text: str


class MotivationResponse(BaseModel):
    response: str

app.add_middleware(
        CORSMiddleware,
        allow_origins = ["*"],
        allow_methods = ["*"],
        allow_headers = ["*"],
        allow_credentials = True
        )


@app.post("/motivate", response_model=MotivationResponse)
def motivate(req: MotivationRequest):
    user_text = req.text.strip()

    #Fake logic for now
    if "clean" in user_text.lower():
        reply = (
                 "No you're not. That's avoidance.\nOpen the document and write one ugly paragraph.\n20 minutes. Start now."
                )

    else:
        reply = (
                 "You've got this.\nStart with the smallest real step.\n20 minutes. Go."
                )

    return {"response": reply}


