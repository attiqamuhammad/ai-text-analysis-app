from Backend.services.sentiment import analyze_sentiment
from Backend.services.tone import analyze_tone
from Backend.services.safety import analyze_safety
from Backend.services.ner import analyze_ner
from Backend.services.key_phrases import extract_key_phrases
from Backend.services.pii import analyze_pii
from Backend.services.topics import extract_topics
from Backend.services.content_aware import analyze_content_aware
from Backend.services.summary import generate_summary


def analyze_text_with_agent(text: str) -> dict:
    """
    Run all text analysis tools and combine their results.
    """

    return {
        "sentiment": analyze_sentiment(text),
        "tone": analyze_tone(text),
        "safety": analyze_safety(text),
        "entities": analyze_ner(text),
        "key_phrases": extract_key_phrases(text),
        "pii": analyze_pii(text),
        "topics": extract_topics(text),
        "content_aware": analyze_content_aware(text),
        "summary": generate_summary(text),
    }