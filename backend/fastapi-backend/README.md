# FastAPI PDF Processing Backend

This project is a FastAPI backend for handling PDF uploads, text extraction, and content generation. It provides a set of API endpoints to facilitate the processing of PDF documents and the generation of various outputs.

## Project Structure

```
fastapi-backend
├── app
│   ├── api
│   │   ├── endpoints
│   │   │   └── pdf.py
│   │   └── __init__.py
│   ├── core
│   │   ├── config.py
│   │   └── __init__.py
│   ├── models
│   │   └── __init__.py
│   ├── services
│   │   ├── pdf_processing.py
│   │   └── __init__.py
│   ├── main.py
│   └── __init__.py
├── tests
│   ├── test_pdf.py
│   └── __init__.py
├── Dockerfile
├── requirements.txt
└── README.md
```

## Features

- **PDF Upload**: Upload PDF files to the server for processing.
- **Text Extraction**: Extract text from uploaded PDFs using libraries like pdfplumber or PyMuPDF.
- **Content Generation**: Generate graphical abstracts and short-form content from the extracted text.
- **API Endpoints**:
  - `POST /upload_pdf`: Upload a PDF file.
  - `GET /summary/{paper_id}`: Retrieve the processed summary.
  - `GET /visual/{paper_id}`: Retrieve the generated visual.
  - `GET /short_content/{paper_id}`: Retrieve the generated short-form content.

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd fastapi-backend
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the application:
   ```
   uvicorn app.main:app --reload
   ```

4. Access the API documentation at `http://localhost:8000/docs`.

## Testing

To run the tests, use:
```
pytest tests/
```

## Docker

To build and run the Docker container:
```
docker build -t fastapi-pdf-backend .
docker run -p 8000:8000 fastapi-pdf-backend
```

## License

This project is licensed under the MIT License. See the LICENSE file for details.