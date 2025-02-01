from PIL import Image, ImageDraw, ImageFont
import textwrap
import os

def generate_graphical_abstract(summary_data: dict, output_path: str) -> str:
    # Create a blank image with white background
    width, height = 800, 600
    image = Image.new('RGB', (width, height), 'white')
    draw = ImageDraw.Draw(image)

    # Load a font
    font = ImageFont.load_default()

    # Define text position and wrapping
    text = summary_data.get('summary', '')
    wrapped_text = textwrap.fill(text, width=70)
    text_position = (50, 50)

    # Draw the text on the image
    draw.text(text_position, wrapped_text, fill='black', font=font)

    # Ensure the output directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Save the image
    image.save(output_path)

    return output_path