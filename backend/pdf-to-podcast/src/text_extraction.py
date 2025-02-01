def extract_text_from_pdf(pdf_path: str) -> str:
    import fitz  # PyMuPDF

    text = ""
    try:
        pdf_document = fitz.open(pdf_path)
        for page_num in range(len(pdf_document)):
            page = pdf_document[page_num]
            text += page.get_text()
        pdf_document.close()
    except Exception as e:
        print(f"Error extracting text from PDF: {e}")
    
    return text.strip()