from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel

import shutil
import os


app = FastAPI(title="Enterprise RAG Assistant")


class QueryRequest(BaseModel):
    question: str


@app.get("/")
def home():
    return {
        "message": "Enterprise RAG Assistant API is running",
        "status": "live"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "service": "enterprise-rag-assistant"
    }


@app.post("/ask")
def ask_question(request: QueryRequest):
    return {
        "question": request.question,
        "answer": "Deployment version is live. Full RAG retrieval works locally. Cloud retrieval is disabled on Render Free due to memory limits.",
        "sources": []
    }


@app.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    upload_dir = "backend/rag/documents"
    os.makedirs(upload_dir, exist_ok=True)

    file_path = os.path.join(upload_dir, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {
        "message": "File uploaded successfully. Cloud indexing is disabled on Render Free due to memory limits.",
        "filename": file.filename,
        "path": file_path
    }