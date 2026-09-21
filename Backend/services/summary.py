import re


def generate_summary(text: str) -> dict:
    """
    Generate a clean factual summary using only the user's text.
    """

    text = text.strip()

    if not text:
        return {
            "summary": "Analysis could not be completed"
        }

    # Clean extra spaces
    text = re.sub(r"\s+", " ", text)

    # Split into sentences while preserving punctuation
    sentences = re.split(r"(?<=[.!?])\s+", text)

    sentences = [
        sentence.strip()
        for sentence in sentences
        if sentence.strip()
    ]

    if not sentences:
        return {
            "summary": "None detected"
        }

    # Use the first two complete sentences
    summary = " ".join(sentences[:2])

    return {
        "summary": summary
    }