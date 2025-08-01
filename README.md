# HackRx 6.0 - Intelligent Query Retrieval System

FastAPI-based implementation to answer insurance queries using document analysis.

## Endpoint
`POST /api/v1/hackrx/run`

## Request Format
```json
{
  "documents": "<PDF URL>",
  "questions": ["question 1", "question 2", ...]
}
```

## Response Format
```json
{
  "answers": ["answer 1", "answer 2", ...]
}
```

## Run locally
```bash
uvicorn app.main:app --host 0.0.0.0 --port 10000
```
