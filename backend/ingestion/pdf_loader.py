from pypdf import PdfReader
from pdf2image import convert_from_path, pdfinfo_from_path
import pytesseract
import os
import hashlib

POPPLER_PATH = r"C:\Users\deeks\Downloads\Release-26.02.0-0\poppler-26.02.0\Library\bin"


def get_cache_file(pdf_path):
    os.makedirs("backend/rag/cache", exist_ok=True)

    filename = os.path.basename(pdf_path)
    file_hash = hashlib.md5(pdf_path.encode()).hexdigest()

    return f"backend/rag/cache/{filename}_{file_hash}.txt"


def load_pdf(pdf_path):
    cache_file = get_cache_file(pdf_path)

    if os.path.exists(cache_file) and os.path.getsize(cache_file) > 0:
        print(f"Loading OCR cache for {pdf_path}...")

        with open(cache_file, "r", encoding="utf-8") as f:
            return f.read()

    text = ""

    try:
        reader = PdfReader(pdf_path)

        for page in reader.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

    except Exception as e:
        print("Normal PDF extraction failed:", e)

    if len(text.strip()) < 100:
        print("Scanned PDF detected. Running OCR...")

        pytesseract.pytesseract.tesseract_cmd = (
            r"C:\Program Files\Tesseract-OCR\tesseract.exe"
        )

        info = pdfinfo_from_path(
            pdf_path,
            poppler_path=POPPLER_PATH
        )

        total_pages = info["Pages"]
        text = ""

        for page_num in range(1, total_pages + 1):
            print(f"Processing page {page_num}/{total_pages}...")

            page = convert_from_path(
                pdf_path,
                first_page=page_num,
                last_page=page_num,
                poppler_path=POPPLER_PATH
            )[0]

            text += pytesseract.image_to_string(page) + "\n"

    print("Saving OCR cache...")

    with open(cache_file, "w", encoding="utf-8") as f:
        f.write(text)

    print("OCR cache saved.")

    return text