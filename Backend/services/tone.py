import re


TONE_KEYWORDS = {
    "Motivated": [
        "work hard",
        "working hard",
        "achieve",
        "goal",
        "goals",
        "dream",
        "dreams",
        "success",
        "improve",
        "growth",
        "determined",
        "努力",
    ],
    "Happy": [
        "happy",
        "glad",
        "joy",
        "excited",
        "love",
        "wonderful",
        "amazing",
    ],
    "Grateful": [
        "thank",
        "thanks",
        "grateful",
        "thankful",
        "appreciate",
        "appreciated",
    ],
    "Angry": [
        "angry",
        "furious",
        "hate",
        "ridiculous",
        "unacceptable",
    ],
    "Sad": [
        "sad",
        "unhappy",
        "cry",
        "lonely",
        "disappointed",
        "heartbroken",
    ],
    "Concerned": [
        "worried",
        "worry",
        "concern",
        "concerned",
        "afraid",
        "fear",
        "problem",
        "issue",
    ],
    "Professional": [
        "report",
        "meeting",
        "project",
        "business",
        "company",
        "proposal",
        "client",
    ],
}


def analyze_tone(text: str) -> dict:
    """
    Detect the general tone of the provided text.
    """

    text_lower = text.lower()
    detected_tones = []

    for tone, keywords in TONE_KEYWORDS.items():
        for keyword in keywords:
            if re.search(r"\b" + re.escape(keyword) + r"\b", text_lower):
                detected_tones.append(tone)
                break

    if not detected_tones:
        detected_tones.append("Neutral")

    return {
        "tone": detected_tones[0],
        "detected_tones": detected_tones,
    }