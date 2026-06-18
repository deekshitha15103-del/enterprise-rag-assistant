from pdf2image import convert_from_path
import pytesseract

pdf_path = r"backend/rag/book.pdf"

POPPLER_PATH = r"C:\Users\deeks\Downloads\Release-26.02.0-0\poppler-26.02.0\Library\bin"

pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)

pages = convert_from_path(
    pdf_path,
    first_page=1,
    last_page=1,
    poppler_path=POPPLER_PATH
)

text = pytesseract.image_to_string(pages[0])

print("\nFIRST 1000 CHARS:\n")
print(text[:1000])