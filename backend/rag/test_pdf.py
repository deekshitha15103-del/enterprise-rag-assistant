from backend.rag.pdf_loader import load_pdf

text = load_pdf(
    r"backend/rag/book.pdf"
)

print(text[:3000])