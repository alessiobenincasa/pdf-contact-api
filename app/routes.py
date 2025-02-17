# app/routes.py
from fastapi import APIRouter, UploadFile, File, HTTPException
from app.services import extract_text_from_pdf

router = APIRouter()

@router.post("/upload/")
async def upload_pdf(file: UploadFile = File(...)):
    if file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="Le fichier doit être un PDF")
    

    pdf_bytes = await file.read()
    
    text = extract_text_from_pdf(pdf_bytes)
    

    return {"filename": file.filename, "extracted_text": text}


