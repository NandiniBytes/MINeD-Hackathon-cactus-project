def translate_and_generate(text: str, target_language: str) -> str:
    from googletrans import Translator
    from voice_generation import generate_voiceover

    # Initialize the translator
    translator = Translator()

    # Translate the text
    translated_text = translator.translate(text, dest=target_language).text

    # Generate voiceover for the translated text
    generate_voiceover(translated_text, target_language)

    return translated_text