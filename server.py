from main import process
from main import classify
from fastapi import FastAPI
from main import classify_multiple

app = FastAPI()

@app.get("/api/nlp/process")
async def nlp_process(data: str):
    return process(data)

@app.get("/api/nlp/classify")
async def nlp_classify(data: str):
    return classify(data)

@app.get("/api/nlp/classify_into_multiple")
async def nlp_classify_into_multiple(data: str):
    return classify_multiple(data)
