Enterprise RAG Assistant

Overview

Enterprise RAG Assistant is a Retrieval-Augmented Generation (RAG) system built using FastAPI, FAISS, Sentence Transformers, Streamlit, OCR, and Ollama.

The application allows users to upload one or more PDF documents, automatically extract text (including scanned PDFs using OCR), generate embeddings, store them in a FAISS vector database, and ask natural language questions against the knowledge base.

Answers are generated using Llama 3.2 through Ollama and include source references from the uploaded documents.



Live Demo & Deployment Notes

GitHub Repository

https://github.com/deekshitha15103-del/enterprise-rag-assistant

Render Deployment

https://enterprise-rag-assistant-j60w.onrender.com

Swagger API Documentation

https://enterprise-rag-assistant-j60w.onrender.com/docs

Deployment Note

The complete Enterprise RAG Assistant runs locally using:

- Ollama
- Llama 3.2
- FAISS Vector Database
- Sentence Transformers
- OCR Pipeline

The hosted Render deployment uses a lightweight configuration because the free Render tier provides only 512 MB RAM, which is insufficient for running the complete local RAG pipeline with Ollama and vector retrieval.

The full-featured version demonstrated in this repository runs successfully in a local environment and includes:

- Multi-PDF Support
- Conversational Memory
- OCR Processing
- Semantic Search
- Source Attribution
- Streamlit Frontend
- Ollama-Based Answer Generation

