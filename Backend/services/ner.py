import re


def analyze_ner(text: str) -> dict:
    """
    Basic Named Entity Recognition.
    Detects simple DATE and ORGANIZATION patterns.
    """

    entities = []

    # Detect dates
    for match in re.finditer(
        r"\b\d{1,2}(?:[-/]\d{1,2}[-/]\d{2,4}|\s+(?:January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{2,4})\b",
        text,
        re.IGNORECASE
    ):
        entities.append({
            "text": match.group(),
            "type": "DATE"
        })

       # Detect common organizations
    organization_pattern = (
        r"\b(?:Microsoft|Google|OpenAI|Apple|Amazon|Meta|IBM)"
        r"\s+(?:Corporation|Company|Inc|Ltd|Technologies|Technology)\b"
    )

    for match in re.finditer(organization_pattern, text):
        entities.append({
            "text": match.group(),
            "type": "ORGANIZATION"
        })

    # Detect common locations
    location_pattern = (
        r"\b(?:Islamabad|Rawalpindi|Lahore|Karachi|"
        r"Peshawar|Quetta|Multan|Faisalabad)\b"
    )

    for match in re.finditer(location_pattern, text, re.IGNORECASE):
        entities.append({
            "text": match.group(),
            "type": "LOCATION"
        })

    return {
        "entities": entities
    }