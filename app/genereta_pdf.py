from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from PIL import Image, ImageDraw, ImageFont
import pytesseract
import io

def create_pdf_without_ocr(filename):
    """
    Crée un PDF contenant uniquement du texte normal (sans OCR).
    """
    c = canvas.Canvas(filename, pagesize=letter)
    c.drawString(100, 750, "Ceci est un fichier PDF de test sans OCR.")
    c.drawString(100, 730, "Il a été généré par Python avec ReportLab.")
    c.save()
    print(f"Le fichier {filename} a été généré sans OCR.")

def create_pdf_with_ocr(filename):
    """
    Crée un PDF avec du texte généré sous forme d'image, pour un usage OCR.
    """
    # Créer une image contenant du texte
    img = Image.new('RGB', (612, 792), color='white')
    d = ImageDraw.Draw(img)
    font = ImageFont.load_default()

    text = "Ceci est un fichier PDF de test avec OCR simulé."
    d.text((100, 750), text, fill=(0, 0, 0), font=font)

    # Sauvegarder l'image en mémoire
    img_path = "/tmp/temp_image.png"
    img.save(img_path)

    # Convertir l'image en PDF
    c = canvas.Canvas(filename, pagesize=letter)
    c.drawImage(img_path, 0, 0, width=612, height=792)
    c.save()

    print(f"Le fichier {filename} a été généré avec OCR simulé.")

if __name__ == "__main__":
    create_pdf_without_ocr("test_without_ocr.pdf")
    create_pdf_with_ocr("test_with_ocr.pdf")
