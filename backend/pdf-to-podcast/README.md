# PDF to Podcast

This project converts research papers in PDF format into podcast-style audio summaries. It integrates text extraction, summarization, voice generation, and multilingual output to provide a seamless experience for users.

## Features

- **Text Extraction**: Extracts text from PDF files using libraries like PyMuPDF, pdfplumber, or pdfminer.six.
- **Summarization**: Utilizes LLM-based models (e.g., GPT-4, T5, BART) to create concise summaries of the extracted text.
- **Voice Generation**: Converts the summarized text into speech using TTS APIs such as Edge TTS, Google TTS, or OpenAI’s TTS API.
- **Multilingual Output**: Translates the text and generates audio output in various languages.

## Installation

To install the required dependencies, run:

```
pip install -r requirements.txt
```

## Usage

1. Place your PDF file in the appropriate directory.
2. Run the main script:

```
python src/main.py <path_to_pdf>
```

3. The output will be an audio file summarizing the content of the PDF.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.