from PyPDF2 import PdfReader

def extract_text(pdf_path: str) -> str:
    text = ""
    try:
        with open(pdf_path, 'rb') as file:
            reader = PdfReader(file)
            for page in reader.pages:
                text += page.extract_text() or ""
    except Exception as e:
        raise RuntimeError(f"Error extracting text from {pdf_path}: {e}")
    return text