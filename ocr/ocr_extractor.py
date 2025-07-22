import pytesseract
from pdf2image import convert_from_path
from PIL import Image
import os

def extract_text_from_pdf(pdf_path):
    images = convert_from_path(pdf_path)
    full_text = ""
    for img in images:
        text = pytesseract.image_to_string(img)
        full_text += text + "\n"
    return full_text

if __name__ == "__main__":
    pdf_path = "../data/sample_insurance_doc.pdf"
    text = extract_text_from_pdf(pdf_path)
    print(text)
