import re


TOPIC_KEYWORDS = {
    "Artificial Intelligence": [
        "artificial intelligence",
        "machine learning",
        "deep learning",
        "large language model",
        "llm",
        "generative ai",
    ],

    "Business": [
        "business",
        "customer",
        "sales",
        "marketing",
        "revenue",
        "company",
    ],

    "Technology": [
        "technology",
        "software",
        "computer",
        "application",
        "app",
        "digital",
    ],

    "Education": [
        "education",
        "course",
        "student",
        "school",
        "university",
        "class",
        "teacher",
    ],

    "Finance": [
        "money",
        "finance",
        "bank",
        "investment",
        "trading",
        "stock",
    ],

    "Health": [
        "health",
        "medical",
        "doctor",
        "hospital",
        "medicine",
    ],
}


def extract_topics(text: str) -> dict:
    text_lower = text.lower()

    topics = []

    for topic, keywords in TOPIC_KEYWORDS.items():
        for keyword in keywords:
            pattern = r"\b" + re.escape(keyword) + r"\b"

            if re.search(pattern, text_lower):
                topics.append(topic)
                break

    return {
        "topics": topics if topics else ["None detected"]
    }



























































