# app/routes.py

from fastapi import APIRouter, UploadFile, File, HTTPException
from app.services import extract_text_from_pdf
from app.llm import extract_contacts_with_hf
import logging

router = APIRouter()

MAX_FILE_SIZE = 10 * 1024 * 1024  # 10 Mo

@router.post("/upload/")
async def upload_pdf(file: UploadFile = File(...)):
    if file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="Le fichier doit être un PDF")

    pdf_bytes = await file.read()
    if len(pdf_bytes) > MAX_FILE_SIZE:
        raise HTTPException(status_code=400, detail="Le fichier est trop volumineux (max 10 Mo)")

    try:
        text = extract_text_from_pdf(pdf_bytes)
        if not text.strip():
            raise HTTPException(status_code=400, detail="Aucun texte n'a été extrait du fichier PDF")

        contacts = extract_contacts_with_hf(text)

        return {
            "filename": file.filename,
            "extracted_text": text,
            "contacts": contacts
        }

    except Exception as e:
        logging.error(f"Erreur lors du traitement du fichier PDF : {str(e)}")
        raise HTTPException(status_code=500, detail="Erreur lors du traitement du fichier PDF")

@router.post("/check-upload/")
async def check_upload(file: UploadFile = File(...)):
    if file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="Le fichier doit être un PDF")

    return {
        "filename": file.filename,
        "content_type": file.content_type,
        "size": len(await file.read())
    }
