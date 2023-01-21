import json
import requests
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from io import BytesIO
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

origins = [
    "https://zoociety.xyz",
    "http://localhost",
    "http://localhost:3000",
    "https://lilfarmboy.xyz"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"message": "Zoociety AI"}


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


@app.get("/dialogue")
def chat(prompt: str):

    output = requests.request(
        "POST",
        "https://api-inference.huggingface.co/models/microsoft/DialoGPT-medium",
        headers={"Authorization": f"Bearer {API_TOKEN}"},
        data=json.dumps(prompt),
    )

    print(output.content)

    return output.content


@app.get("/anime")
def generate(prompt: str):
    output = requests.request(
        "POST",
        "https://api-inference.huggingface.co/models/hakurei/waifu-diffusion",
        headers={"Authorization": f"Bearer {API_TOKEN}"},
        data=json.dumps(prompt),
    )

    return StreamingResponse(BytesIO(output.content), media_type="image/png")


@app.get("/cyberpunk")
def generate(prompt: str):
    output = requests.request(
        "POST",
        "https://api-inference.huggingface.co/models/DGSpitzer/Cyberpunk-Anime-Diffusion",
        headers={"Authorization": f"Bearer {API_TOKEN}"},
        data=json.dumps(prompt),
    )

    return StreamingResponse(BytesIO(output.content), media_type="image/png")
