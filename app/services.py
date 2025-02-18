# app/services.py

import platform
from tempfile import TemporaryDirectory
from pathlib import Path
import re
import pytesseract
from pdf2image import convert_from_path
from PIL import Image
from io import BytesIO

def extract_text_from_pdf(pdf_bytes: bytes) -> str:
    """
    Extrait le texte d'un PDF à partir de ses octets en utilisant la conversion en images
    puis l'OCR (pytesseract). Retourne le texte extrait.
    """
    with TemporaryDirectory() as tempdir:
        pdf_file_path = Path(tempdir) / "temp.pdf"
        with open(pdf_file_path, "wb") as f:
            f.write(pdf_bytes)
        
        pdf_pages = convert_from_path(str(pdf_file_path), 500)
        extracted_text = ""
        
        for page in pdf_pages:
            image_path = Path(tempdir) / "temp.jpg"
            page.save(image_path, "JPEG")
            
            page_text = pytesseract.image_to_string(Image.open(image_path))
            page_text = page_text.replace("-\n", "")
            extracted_text += page_text + "\n"
    
    return extracted_text
