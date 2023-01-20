import json
import requests
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from io import BytesIO

app = FastAPI()


@app.get("/")
def read_root():
    return {"ZOOCIETY": "AI"}


API_TOKEN = "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"
API_URL = "https://api-inference.huggingface.co/models/dreamlike-art/dreamlike-photoreal-2.0"

headers = {"Authorization": f"Bearer {API_TOKEN}"}


@app.get("/photoreal")
def generate(prompt: str):
    output = requests.request(
        "POST",
        "https://api-inference.huggingface.co/models/dreamlike-art/dreamlike-photoreal-2.0",
        headers={"Authorization": f"Bearer {API_TOKEN}"},
        data=json.dumps(prompt),
    )

    return StreamingResponse(BytesIO(output.content), media_type="image/png")


@app.get("/diffusion")
def generate(prompt: str):
    output = requests.request(
        "POST",
        "https://api-inference.huggingface.co/models/runwayml/stable-diffusion-v1-5",
        headers={"Authorization": f"Bearer {API_TOKEN}"},
        data=json.dumps(prompt),
    )

    return StreamingResponse(BytesIO(output.content), media_type="image/png")
