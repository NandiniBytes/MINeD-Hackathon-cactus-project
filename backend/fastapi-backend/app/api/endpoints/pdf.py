from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import FileResponse
from app.services.pdf_processing import extract_text, generate_graphical_abstract, generate_short_content
import os

router = APIRouter()

UPLOAD_DIR = "input_pdfs"
OUTPUT_DIR = "output"

@router.post("/upload_pdf/")
async def upload_pdf(file: UploadFile = File(...)):
    if not file.filename.endswith('.pdf'):
        raise HTTPException(status_code=400, detail="Invalid file type. Only PDF files are allowed.")
    
    file_location = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_location, "wb+") as file_object:
        file_object.write(await file.read())
    
    # Process the PDF (text extraction, graphical abstract generation, etc.)
    extracted_text = extract_text(file_location)
    paper_id = file.filename.split('.')[0]  # Use filename without extension as paper_id
    generate_graphical_abstract(extracted_text, paper_id)
    generate_short_content(extracted_text, paper_id)

    return {"filename": file.filename, "paper_id": paper_id}

@router.get("/get_summary/{paper_id}")
async def get_summary(paper_id: str):
    summary_path = os.path.join(OUTPUT_DIR, paper_id, "summary.json")
    if not os.path.exists(summary_path):
        raise HTTPException(status_code=404, detail="Summary not found.")
    return FileResponse(summary_path)

@router.get("/get_visual/{paper_id}")
async def get_visual(paper_id: str):
    visual_path = os.path.join(OUTPUT_DIR, paper_id, "summary.png")
    if not os.path.exists(visual_path):
        raise HTTPException(status_code=404, detail="Visual not found.")
    return FileResponse(visual_path)

@router.get("/get_short_content/{paper_id}")
async def get_short_content(paper_id: str):
    short_content_path = os.path.join(OUTPUT_DIR, paper_id)
    if not os.path.exists(short_content_path):
        raise HTTPException(status_code=404, detail="Short content not found.")
    return {"short_content_path": short_content_path}