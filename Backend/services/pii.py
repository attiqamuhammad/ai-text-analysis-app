import re


def analyze_pii(text: str) -> dict:
    """
    Lightweight PII detection for email, phone, and common ID patterns.
    """

    pii_entities = []

    patterns = {
        "EMAIL_ADDRESS": r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b",
        "PHONE_NUMBER": r"\b(?:\+92|0092|0)?3\d{9}\b",
        "CNIC": r"\b\d{5}-\d{7}-\d\b",
    }

    for entity_type, pattern in patterns.items():
        for match in re.finditer(pattern, text):
            pii_entities.append({
                "type": entity_type,
                "text": match.group(),
            })

    return {
        "pii_detected": pii_entities
    }