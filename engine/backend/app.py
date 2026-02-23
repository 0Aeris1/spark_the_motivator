
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from ai import generate_motivation
from schemas import MotivationRequest, MotivationResponse

app = FastAPI()


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


