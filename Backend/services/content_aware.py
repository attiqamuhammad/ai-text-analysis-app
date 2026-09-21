import re


CONTENT_TYPES = {
    "Personal Information": [
        "email",
        "phone",
        "telephone",
        "address",
        "cnic",
        "date of birth",
    ],

    "Business": [
        "business",
        "customer",
        "sales",
        "marketing",
        "company",
        "revenue",
    ],

    "Technology": [
        "artificial intelligence",
        "machine learning",
        "technology",
        "software",
        "computer",
        "application",
        "digital",
    ],

    "Education": [
        "education",
        "course",
        "student",
        "school",
        "university",
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


def analyze_content_aware(text: str) -> dict:
    text_lower = text.lower()
    detected_types = []

    for content_type, keywords in CONTENT_TYPES.items():
        for keyword in keywords:
            if re.search(r"\b" + re.escape(keyword) + r"\b", text_lower):
                detected_types.append(content_type)
                break

    return {
        "content_types": (
            detected_types
            if detected_types
            else ["General"]
        )
    }