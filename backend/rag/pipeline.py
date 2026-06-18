from backend.rag.pdf_loader import load_pdf
from backend.rag.splitter import split_text
from backend.rag.embeddings import get_embeddings
from backend.rag.vectorstore import create_vectorstore

pdf_path = r"backend/rag/book.pdf"

print("Loading PDF...")
text = load_pdf(pdf_path)

print("Splitting text...")
chunks = split_text(text)

print("Creating embeddings...")
embeddings = get_embeddings(chunks)

print("Building vector store...")
index = create_vectorstore(embeddings)

print("DONE ✅")
print("Chunks:", len(chunks))