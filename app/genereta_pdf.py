import random
import os
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from PIL import Image, ImageDraw, ImageFont

def generate_random_contact():
    """
    Génère aléatoirement des informations de contact.
    """
    first_names = ["Jean", "Marie", "Pierre", "Sophie", "Luc", "Anne", "Julien", "Camille", "Nathalie", "Eric"]
    last_names = ["Dupont", "Martin", "Durand", "Lefevre", "Moreau", "Laurent", "Girard", "Roux", "Bertrand", "Faure"]
    streets = ["rue de Paris", "avenue des Champs", "boulevard Saint-Germain", "rue Lafayette", "rue Victor Hugo"]
    cities = ["Paris", "Lyon", "Marseille", "Nice", "Bordeaux", "Toulouse"]
    
    name = random.choice(first_names) + " " + random.choice(last_names)
    email = name.lower().replace(" ", ".") + "@example.com"
    telephone = "+33 " + "".join(str(random.randint(0, 9)) for _ in range(9))
    street_number = random.randint(1, 200)
    street = random.choice(streets)
    city = random.choice(cities)
    zipcode = random.randint(75000, 75999) if city == "Paris" else random.randint(10000, 99999)
    address = f"{street_number} {street}, {zipcode} {city}"
    
    return name, email, telephone, address

def create_mixed_contact_pdf(filename, num_pages=4):
    """
    Crée un PDF multi-pages contenant un mélange de pages avec texte natif
    et de pages avec texte sous forme d'image (simulant un contenu nécessitant l'OCR).
    Chaque page affiche des informations de contact générées aléatoirement.
    """
    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter
    
    for i in range(num_pages):
        name, email, telephone, address = generate_random_contact()
        contact_text = (
            f"Nom: {name}\n"
            f"Email: {email}\n"
            f"Téléphone: {telephone}\n"
            f"Adresse: {address}"
        )
        
        use_native = random.choice([True, False])
        
        if use_native:
            y = height - 100
            for line in contact_text.split("\n"):
                c.drawString(100, y, line)
                y -= 20
            c.drawString(100, y - 20, "(Texte natif)")
        else:
            img = Image.new('RGB', (int(width), int(height)), color='white')
            d = ImageDraw.Draw(img)
            font = ImageFont.load_default()
            y = 100
            for line in contact_text.split("\n"):
                d.text((50, y), line, fill="black", font=font)
                y += 20
            d.text((50, y + 20), "(Texte dans une image pour OCR)", fill="black", font=font)
            
            temp_img_path = "temp_contact.png"
            img.save(temp_img_path)
            c.drawImage(temp_img_path, 0, 0, width=width, height=height)
            os.remove(temp_img_path)
        
        c.showPage()
    
    c.save()
    print(f"Le PDF '{filename}' a été généré avec {num_pages} pages mixtes.")

if __name__ == "__main__":
    create_mixed_contact_pdf("mixed_contacts.pdf", num_pages=4)

