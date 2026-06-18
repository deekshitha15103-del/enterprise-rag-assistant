# Enterprise RAG Assistant

## Overview

Enterprise RAG Assistant is a Retrieval-Augmented Generation (RAG) system built using FastAPI, FAISS, OCR, and Sentence Transformers.

The system allows users to upload PDF documents, extract text using OCR when necessary, generate vector embeddings, store them in a FAISS vector database, and retrieve relevant information through semantic search.

---

## Features

* PDF Upload API
* OCR Support for Scanned PDFs
* Automatic Text Chunking
* Sentence Transformer Embeddings
* FAISS Vector Search
* Source-Aware Retrieval
* FastAPI Backend
* Swagger Documentation
* Persistent Chunk Storage
* Persistent FAISS Index Storage

---

## Architecture

PDF Document

↓

OCR / Text Extraction

↓

Text Chunking

↓

Embedding Generation

↓

FAISS Vector Database

↓

Retriever

↓

LLM Layer

↓

API Response

---

## Tech Stack

* Python 3.11
* FastAPI
* FAISS
* Sentence Transformers
* PyPDF
* Tesseract OCR
* PDF2Image
* Uvicorn

---

## API Endpoints

### GET /

Health Check Endpoint

### POST /upload

Upload and index PDF documents.

### POST /ask

Ask questions against the indexed knowledge base.

---

## Project Structure

backend/

├── api/

├── ingestion/

├── llm/

├── rag/

├── retrieval/

└── utils/

---

## Current Status

Completed:

* OCR Pipeline
* PDF Ingestion
* Vector Search
* Source Tracking
* FastAPI Backend
* GitHub Integration

Planned:

* Real Claude Integration
* Multi-Document Search
* User Authentication
* Chat History
* Cloud Deployment

---

## Author

Deekshitha
