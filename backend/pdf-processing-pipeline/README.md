# PDF Processing Pipeline

## Overview
The PDF Processing Pipeline is a Python-based project designed to automate the extraction, summarization, and visualization of content from PDF documents. This pipeline facilitates the processing of multiple PDFs efficiently, providing a structured output that includes summaries and graphical abstracts.

## Project Structure
```
pdf-processing-pipeline
├── src
│   ├── main.py                # Main processing script
│   ├── text_extraction.py     # Text extraction from PDFs
│   ├── summarization.py        # Summarization of extracted text
│   ├── image_generator.py      # Generation of graphical abstracts
│   └── utils
│       └── __init__.py        # Utility functions
├── config
│   └── config.yaml            # Configuration settings
├── logs
│   └── pipeline.log           # Log file for processing
├── output
│   └── .gitkeep               # Placeholder for output directory
├── requirements.txt           # Project dependencies
└── README.md                  # Project documentation
```

## Installation
To set up the project, clone the repository and install the required dependencies:

```bash
git clone <repository-url>
cd pdf-processing-pipeline
pip install -r requirements.txt
```

## Configuration
Modify the `config/config.yaml` file to set processing parameters, such as input paths and options for the pipeline.

## Usage
To process a PDF file, run the main script with the desired PDF path and output directory:

```bash
python src/main.py <pdf_path> <output_dir>
```

## Features
- **Text Extraction**: Extracts text from PDF files using `text_extraction.py`.
- **Summarization**: Generates a summary of the extracted text (if `summarization.py` is implemented).
- **Graphical Abstract**: Creates a visual representation of the summary using `image_generator.py`.
- **Batch Processing**: Supports processing multiple PDF files simultaneously.
- **Logging**: Tracks progress and errors in `logs/pipeline.log`.

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for details.