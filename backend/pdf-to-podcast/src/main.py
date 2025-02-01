def main():
    import sys
    from text_extraction import extract_text_from_pdf
    from summarization import summarize_text
    from voice_generation import generate_voiceover
    from multilingual_output import translate_and_generate

    if len(sys.argv) < 3:
        print("Usage: python main.py <pdf_path> <language_code>")
        sys.exit(1)

    pdf_path = sys.argv[1]
    language_code = sys.argv[2]

    # Step 1: Extract text from PDF
    extracted_text = extract_text_from_pdf(pdf_path)
    
    # Step 2: Summarize the extracted text
    summary = summarize_text(extracted_text)
    
    # Step 3: Generate voiceover in the specified language
    generate_voiceover(summary, language_code)

    # Optional: Translate and generate audio for multilingual output
    translated_text = translate_and_generate(summary, language_code)
    generate_voiceover(translated_text, language_code)

if __name__ == "__main__":
    main()