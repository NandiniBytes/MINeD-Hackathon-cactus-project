def generate_summary(text: str) -> str:
    # Simple summarization logic (placeholder)
    sentences = text.split('. ')
    summary = '. '.join(sentences[:2])  # Return the first two sentences as a summary
    return summary.strip()