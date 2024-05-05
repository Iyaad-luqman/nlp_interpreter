from fastapi import FastAPI, HTTPException
from llm_processor import process_prompt

app = FastAPI()

@app.get("/api/nlp/process")
async def process(data: str):
    try:
        response_json = await process_prompt(data)
        return response_json
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=500, detail="An unexpected error occurred.")