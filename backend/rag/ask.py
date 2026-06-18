from backend.rag.metadata import save_chunks, load_chunks
from backend.rag.pdf_loader import load_pdf
from backend.rag.splitter import split_text
from backend.rag.embeddings import get_embeddings
from backend.rag.vectorstore import (
    create_vectorstore,
    save_index,
    load_index
)
from backend.retrieval.retriever import search
from backend.rag.llm import generate_answer
from sentence_transformers import SentenceTransformer

pdf_path = r"backend/rag/book.pdf"

print("Loading PDF...")
text = load_pdf(pdf_path)

chunks = load_chunks()

if chunks is None:
    print("Splitting...")
    chunks = split_text(text)

    print("Saving chunks...")
    save_chunks(chunks)

else:
    print("Loaded saved chunks.")

print("Loading embedding model...")
model = SentenceTransformer("all-MiniLM-L6-v2")

index = load_index()

if index is None:
    print("Embedding...")
    embeddings = get_embeddings(chunks)

    print("Creating FAISS index...")
    index = create_vectorstore(embeddings)

    print("Saving FAISS index...")
    save_index(index)

else:
    print("Loaded existing FAISS index.")

print("READY ✅ Ask questions!")

while True:

    query = input("\nAsk: ")

    if query.lower() in ["exit", "quit"]:
        break

    context_chunks = search(
        query,
        model,
        index,
        chunks
    )

    answer = generate_answer(
        query,
        context_chunks
    )

    print("\nANSWER:\n")
    print(answer)