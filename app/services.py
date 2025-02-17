import tempfile
import io
import os
import pdfplumber
from PIL import Image
import pytesseract
from pdf2image import convert_from_path

def extract_text_from_pdf(pdf_bytes: bytes) -> str:
    """
    Extrait le texte d'un PDF passé sous forme d'octets.
    Si le texte natif est présent, il est extrait. Sinon, OCR est effectué sur les pages sans texte natif.
    """
    text = ""

    with pdfplumber.open(io.BytesIO(pdf_bytes)) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
            else:
                text += perform_ocr_for_page(pdf_bytes, page) + "\n"

    return text.strip()

def perform_ocr_for_page(pdf_bytes: bytes, page) -> str:
    """
    Effectue un OCR sur une page spécifique du PDF si aucun texte natif n'est disponible.
    """
    with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as tmp_pdf_file:
        tmp_pdf_file.write(pdf_bytes)
        tmp_pdf_path = tmp_pdf_file.name

    try:
        images = convert_from_path(tmp_pdf_path, first_page=page.page_number, last_page=page.page_number)

        text = image_to_text(images[0])
        return text.strip()
    finally:
        os.remove(tmp_pdf_path)

def image_to_text(image: Image) -> str:
    """
    Utilise Tesseract pour extraire du texte d'une image.
    """
    return pytesseract.image_to_string(image)
