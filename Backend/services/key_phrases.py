from rake_nltk import Rake


CUSTOM_STOPWORDS = {
    "i", "am", "is", "are", "was", "were",
    "my", "me", "we", "our", "you", "your",
    "the", "a", "an", "and", "or", "but",
    "with", "for", "to", "of", "in", "on", "at",
    "this", "that", "these", "those",
    "very", "new", "love",
    "email", "phone", "number",
    "example", "com", "www", "http", "https",
}


def extract_key_phrases(text: str) -> dict:
    """
    Extract concise and meaningful key phrases.
    """

    rake = Rake(
        stopwords=CUSTOM_STOPWORDS,
        min_length=2,
        max_length=4,
    )

    rake.extract_keywords_from_text(text)

    ranked_phrases = rake.get_ranked_phrases()

    phrases = []

    for phrase in ranked_phrases:
        phrase = phrase.strip().lower()

        # Remove unwanted words from the beginning
        words = phrase.split()

        while words and words[0] in CUSTOM_STOPWORDS:
            words.pop(0)

        phrase = " ".join(words)

        if len(words) < 2:
            continue

        if "@" in phrase or ".com" in phrase:
            continue

        if phrase not in phrases:
            phrases.append(phrase)

    return {
        "key_phrases": phrases[:10] if phrases else ["None detected"]
    }