# app/routes.py

from fastapi import APIRouter, Depends, UploadFile, File
from sqlalchemy.orm import Session
from .database import get_db, Document

router = APIRouter()

@router.post("/upload/")
async def upload_document(file: UploadFile = File(...), db: Session = Depends(get_db)):
    # Logic to save the document and extract content
    # For example:
    # contents = await file.read()  # Read the content of the uploaded file
    # document_instance = Document(filename=file.filename, content=contents.decode())
    
    # Save to the database
    # db.add(document_instance)
    # db.commit()
    
    return {"message": "Document uploaded successfully"}
