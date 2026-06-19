from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel

from backend.rag.metadata import load_chunk_records, save_chunk_records
from backend.rag.vectorstore import create_vectorstore, save_index, load_index
from backend.rag.pdf_loader import load_pdf
from backend.rag.splitter import split_text
from backend.rag.embeddings import get_embeddings
from backend.retrieval.retriever import search_with_sources
from backend.rag.llm import generate_answer

from sentence_transformers import SentenceTransformer

import shutil
import os


app = FastAPI(title="Enterprise RAG Assistant")

print("Loading local full RAG system...")

records = load_chunk_records()
chunks = [item["text"] for item in records]

index = load_index()
model = SentenceTransformer("all-MiniLM-L6-v2")

print("Local full RAG system loaded.")


class QueryRequest(BaseModel):
    question: str


@app.get("/")
def home():
    return {
        "message": "Enterprise RAG Assistant API is running",
        "mode": "local-full-rag-ollama"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "service": "enterprise-rag-assistant",
        "mode": "local-full-rag-ollama"
    }


@app.post("/ask")
def ask_question(request: QueryRequest):
    if index is None or len(records) == 0:
        return {
            "question": request.question,
            "answer": "Knowledge base is empty. Please upload and index a PDF first.",
            "sources": []
        }

    retrieved = search_with_sources(
        request.question,
        model,
        index,
        records
    )

    context_chunks = [item["text"] for item in retrieved]

    answer = generate_answer(
        request.question,
        context_chunks
    )

    sources = []

    for item in retrieved:
        sources.append({
            "source": item["source"],
            "chunk_id": item["chunk_id"],
            "preview": item["text"][:300]
        })

    return {
        "question": request.question,
        "answer": answer,
        "sources": sources
    }


@app.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    global records, chunks, index

    upload_dir = "backend/rag/documents"
    os.makedirs(upload_dir, exist_ok=True)

    file_path = os.path.join(upload_dir, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    print("Processing uploaded PDF...")

    text = load_pdf(file_path)
    new_chunks = split_text(text)

    start_id = len(records)

    new_records = []

    for i, chunk in enumerate(new_chunks):
        new_records.append({
            "chunk_id": start_id + i,
            "source": file.filename,
            "text": chunk
        })

    records.extend(new_records)
    chunks = [item["text"] for item in records]

    save_chunk_records(records)

    embeddings = get_embeddings(chunks)

    index = create_vectorstore(embeddings)

    save_index(index)

    return {
        "message": "File uploaded, indexed, and added to knowledge base successfully",
        "filename": file.filename,
        "new_chunks_added": len(new_chunks),
        "total_chunks": len(chunks)
    }