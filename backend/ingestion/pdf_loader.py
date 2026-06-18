from pdf2image import convert_from_path
from pytesseract import image_to_string

POPPLER_PATH = r"C:\Users\deeks\Downloads\Release-26.02.0-0\poppler-26.02.0\Library\bin"

def load_pdf(pdf_path):
    pages = convert_from_path(pdf_path, poppler_path=POPPLER_PATH)

    text = ""
    for page in pages:
        text += image_to_string(page) + "\n"

    return text