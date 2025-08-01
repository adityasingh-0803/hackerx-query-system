from fastapi import FastAPI, Request, HTTPException
from pydantic import BaseModel
from app.utils import process_query

app = FastAPI()

class HackRxRequest(BaseModel):
    documents: str
    questions: list[str]

@app.post("/api/v1/hackrx/run")
async def run_query(payload: HackRxRequest, request: Request):
    auth = request.headers.get("authorization", "")
    if not auth.endswith("aff4ddc3"):
        raise HTTPException(status_code=403, detail="Invalid token")
    answers = process_query(payload.documents, payload.questions)
    return {"answers": answers}
