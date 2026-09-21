import re


CATEGORIES = {
    "hate": [
        r"\bhate (all|those|these|them)\b",
        r"\bkill (all|those|these|them)\b",
        r"\bracist\b",
        r"\bslur\b",
        r"\bwhite supremacist\b",
        r"\bgenocide\b",
    ],
    "sexual": [
        r"\bsexually explicit\b",
        r"\bsexual assault\b",
        r"\bsexual abuse\b",
        r"\bnude\b",
        r"\bnudity\b",
        r"\bporn\b",
        r"\bpornography\b",
    ],
    "violence": [
        r"\bkill someone\b",
        r"\bkill (all|those|them)\b",
        r"\bmurder\b",
        r"\bshoot someone\b",
        r"\bstab someone\b",
        r"\battack someone\b",
        r"\bweapon\b",
        r"\bviolent\b",
    ],
    "self_harm": [
        r"\bsuicide\b",
        r"\bkill myself\b",
        r"\bhurt myself\b",
        r"\bself[- ]harm\b",
        r"\bend my life\b",
    ],
}


def _detect_category(text: str, patterns: list[str]) -> dict:
    for pattern in patterns:
        if re.search(pattern, text, re.IGNORECASE):
            return {
                "severity": 1,
                "status": "detected",
            }

    return {
        "severity": 0,
        "status": "none detected",
    }


def analyze_safety(text: str) -> dict:
    """
    Lightweight safety analysis for common harmful-content patterns.
    """

    results = {
        category: _detect_category(text, patterns)
        for category, patterns in CATEGORIES.items()
    }

    if any(
        result["severity"] > 0
        for result in results.values()
    ):
        overall = "Risk"
    else:
        overall = "Safe"

    return {
        "overall": overall,
        "categories": results,
    }