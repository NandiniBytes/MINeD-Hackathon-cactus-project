def clean_text(text: str) -> str:
    """Cleans the extracted text by removing unnecessary whitespace and special characters."""
    return ' '.join(text.split())

def save_audio_file(audio_content: bytes, file_path: str) -> None:
    """Saves the generated audio content to a specified file path."""
    with open(file_path, 'wb') as audio_file:
        audio_file.write(audio_content)

def load_audio_file(file_path: str) -> bytes:
    """Loads an audio file from the specified file path."""
    with open(file_path, 'rb') as audio_file:
        return audio_file.read()

def generate_file_name(base_name: str, extension: str) -> str:
    """Generates a file name with the specified base name and extension."""
    return f"{base_name}.{extension}"