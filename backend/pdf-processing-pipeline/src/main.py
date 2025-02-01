from pathlib import Path
import json
import os
import logging
import asyncio
from text_extraction import extract_text
from summarization import generate_summary
from image_generator import generate_graphical_abstract

# Configure logging
logging.basicConfig(filename='logs/pipeline.log', level=logging.INFO)

async def process_paper(pdf_path: str, output_dir: str) -> dict:
    results = {}
    try:
        # Validate input
        if not Path(pdf_path).is_file():
            raise FileNotFoundError(f"PDF file not found: {pdf_path}")

        # Create output directory
        paper_name = Path(pdf_path).stem
        output_path = Path(output_dir) / paper_name
        output_path.mkdir(parents=True, exist_ok=True)

        # Step 1: Extract text
        logging.info(f"Extracting text from {pdf_path}")
        extracted_text = await asyncio.to_thread(extract_text, pdf_path)
        results['extracted_text'] = extracted_text

        # Step 2: Generate summary
        logging.info("Generating summary")
        summary = await asyncio.to_thread(generate_summary, extracted_text)
        results['summary'] = summary

        # Step 3: Create graphical abstract
        logging.info("Creating graphical abstract")
        image_path = output_path / 'summary.png'
        await asyncio.to_thread(generate_graphical_abstract, {'summary': summary}, str(image_path))
        results['image_path'] = str(image_path)

        # Save summary to JSON
        summary_path = output_path / 'summary.json'
        with open(summary_path, 'w') as json_file:
            json.dump({'summary': summary}, json_file)
        results['summary_path'] = str(summary_path)

        logging.info(f"Processing completed for {pdf_path}")

    except Exception as e:
        logging.error(f"Error processing {pdf_path}: {e}")
        results['error'] = str(e)

    return results

async def main(pdf_paths: list, output_dir: str):
    tasks = [process_paper(pdf_path, output_dir) for pdf_path in pdf_paths]
    return await asyncio.gather(*tasks)

if __name__ == "__main__":
    # Example usage
    pdf_files = ['path/to/pdf1.pdf', 'path/to/pdf2.pdf']  # Replace with actual paths
    output_directory = 'output'
    asyncio.run(main(pdf_files, output_directory))