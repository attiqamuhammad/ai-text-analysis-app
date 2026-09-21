from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


analyzer = SentimentIntensityAnalyzer()


def analyze_sentiment(text: str) -> dict:
    """
    Analyze sentiment using VADER.

    Returns:
        dict: Sentiment label and compound score.
    """

    scores = analyzer.polarity_scores(text)
    compound = scores["compound"]

    if compound >= 0.05:
        sentiment = "Positive"
    elif compound <= -0.05:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    return {
        "sentiment": sentiment,
        "polarity": round(compound, 3),
    }