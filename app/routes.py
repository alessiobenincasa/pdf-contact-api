from fastapi import APIRouter, UploadFile, File, HTTPException
from app.services import extract_text_from_pdf
from app.llm import extract_contacts_with_hf
import logging

router = APIRouter()

# Définir une taille max (10 Mo ici)
MAX_FILE_SIZE = 10 * 1024 * 1024  # 10MB

@router.post("/upload/")
async def upload_pdf(file: UploadFile = File(...)):
    if file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="Le fichier doit être un PDF")

    # Vérifier la taille du fichier
    pdf_bytes = await file.read()
    if len(pdf_bytes) > MAX_FILE_SIZE:
        raise HTTPException(status_code=400, detail="Le fichier est trop volumineux (max 10 Mo)")

    try:
        # Extraire le texte du PDF
        text = extract_text_from_pdf(pdf_bytes)
        if not text.strip():
            raise HTTPException(status_code=400, detail="Aucun texte n'a été extrait du fichier PDF")

        # Extraire les contacts via LLM
        contacts = extract_contacts_with_hf(text)

        return {
            "filename": file.filename,
            "extracted_text": text,
            "contacts": contacts
        }

    except Exception as e:
        logging.error(f"Erreur lors du traitement du fichier PDF : {str(e)}")
        raise HTTPException(status_code=500, detail="Erreur lors du traitement du fichier PDF")


