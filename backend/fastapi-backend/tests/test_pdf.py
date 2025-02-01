from fastapi.testclient import TestClient
from app.main import app
from app.services.pdf_processing import extract_text, generate_graphical_abstract, generate_short_content

client = TestClient(app)

def test_upload_pdf():
    response = client.post("/api/pdf/upload", files={"file": ("test.pdf", open("input_pdfs/test.pdf", "rb"))})
    assert response.status_code == 200
    assert "paper_id" in response.json()

def test_get_summary():
    paper_id = "test_paper_id"
    response = client.get(f"/api/pdf/summary/{paper_id}")
    assert response.status_code == 200
    assert "summary" in response.json()

def test_get_visual():
    paper_id = "test_paper_id"
    response = client.get(f"/api/pdf/visual/{paper_id}")
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "image/png"

def test_get_short_content():
    paper_id = "test_paper_id"
    response = client.get(f"/api/pdf/short_content/{paper_id}")
    assert response.status_code == 200
    assert "short_content" in response.json()

def test_extract_text():
    text = extract_text("input_pdfs/test.pdf")
    assert isinstance(text, str)
    assert len(text) > 0

def test_generate_graphical_abstract():
    abstract = generate_graphical_abstract("Sample text for graphical abstract")
    assert abstract is not None

def test_generate_short_content():
    content = generate_short_content("Sample text for short content")
    assert content is not None