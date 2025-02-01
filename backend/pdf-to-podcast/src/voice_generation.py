def generate_voiceover(text: str, language: str) -> None:
    import pyttsx3

    engine = pyttsx3.init()
    
    # Set properties before adding anything to speak
    engine.setProperty('rate', 150)  # Speed of speech
    engine.setProperty('volume', 1)  # Volume 0-1

    # Set language if supported
    voices = engine.getProperty('voices')
    if language == 'en':
        engine.setProperty('voice', voices[0].id)  # English voice
    elif language == 'es':
        engine.setProperty('voice', voices[1].id)  # Spanish voice
    # Add more languages as needed

    # Generate audio from text
    engine.save_to_file(text, 'output.mp3')
    engine.runAndWait()