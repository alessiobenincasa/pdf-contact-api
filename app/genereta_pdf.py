from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def create_pdf(filename):
    c = canvas.Canvas(filename, pagesize=letter)
    
 
    c.drawString(100, 750, "Ceci est un fichier PDF de test.")
    c.drawString(100, 730, "Il a été généré par Python avec ReportLab.")
    

    c.save()

if __name__ == "__main__":
    create_pdf("test.pdf")
    print("Le fichier test.pdf a été généré avec succès.")
