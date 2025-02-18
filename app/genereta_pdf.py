from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from PIL import Image, ImageDraw, ImageFont
import pytesseract

def generate_pdf():
    pdf_path = "mixed_contacts_test_v3.pdf"
    
    # Créer un fichier PDF avec du texte natif
    c = canvas.Canvas(pdf_path, pagesize=letter)

    # --- Bloc de texte natif en haut ---
    text_native = (
        "Répertoire des Contacts - Version Vérification\n"
        "------------------------------------------------------------\n"
        "Service Client:\n"
        "  - Nom : Alice Dupont\n"
        "  - Email : alice.dupont@example.fr\n"
        "  - Téléphone : +33 (1) 23-45-67-89\n\n"
        "Support Technique:\n"
        "  - Nom : Bernard Martin\n"
        "  - Email : bernard.martin@techsupport.fr\n"
        "  - Téléphone : +33 (1) 98-76-54-32\n\n"
        "Direction Générale:\n"
        "  - Adresse : 10 Rue de la République, 75001 Paris\n"
        "------------------------------------------------------------\n"
        "Horaires d'ouverture : Lundi à Vendredi, de 8h à 17h."
    )

    text_object = c.beginText(50, 750)
    for line in text_native.split('\n'):
        text_object.textLine(line)
    c.drawText(text_object)

    # --- Zone OCR (image) au milieu ---
    ocr_text = (
        "Département RH & Administratif:\n"
        "------------------------------------------------------------\n"
        "  - Nom : Claire Bernard\n"
        "  - Email : claire.bernard@entreprise.fr\n"
        "  - Téléphone : +33 1 44 55 66 77\n\n"
        "Finances:\n"
        "  - Nom : David Legrand\n"
        "  - Email : d.legrand@finance.fr\n"
        "  - Téléphone : +33 1 11 22 33 44\n\n"
        "Service Marketing:\n"
        "  - Nom : Élodie Petit\n"
        "  - Email : elodie.petit@marketing.fr\n"
        "  - Téléphone : +33 1 55 66 77 88\n"
        "------------------------------------------------------------\n"
        "Pour plus d'informations, visitez notre site web corporate."
    )

    # Créer une image pour le texte OCR
    font = ImageFont.load_default()
    # Taille d'image ajustée pour contenir le texte
    img = Image.new("RGB", (600, 220), color=(255, 255, 255))
    d = ImageDraw.Draw(img)
    y_text = 10
    for line in ocr_text.split('\n'):
        d.text((10, y_text), line, font=font, fill=(0, 0, 0))
        y_text += 15  # Ajustement de l'espacement entre les lignes

    # Sauvegarder l'image générée
    img_path = "ocr_text_image_v2.png"
    img.save(img_path)

    # Insérer l'image OCR dans le PDF (position et taille adaptées)
    c.drawImage(img_path, 50, 500, width=500, height=220)

    # --- Bloc de texte natif en bas ---
    bottom_text = (
        "Note Finale: Ce document a été généré pour vérifier le bon fonctionnement de l'extraction de contacts.\n"
        "  - Nom : Alessio Benincasa \n"
        "  - Email : alessio.ebreet@marketing.fr\n"
        "  - Téléphone : +33 1 95 66 77 88\n"
    )

    bottom_text_object = c.beginText(50, 50)  # Positionné près du bas de la page
    for line in bottom_text.split('\n'):
        bottom_text_object.textLine(line)
    c.drawText(bottom_text_object)

    # Sauvegarder le PDF
    c.save()
    print(f"PDF généré : {pdf_path}")

generate_pdf()
