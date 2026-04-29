from __future__ import annotations

import re


def clean_headline(headline: str) -> str:
    """Normalize a headline into a stable lowercase string."""
    cleaned = re.sub(r"\([^)]*\)", "", headline)
    cleaned = re.sub(r"\[[^]]*\]", "", cleaned)
    cleaned = re.sub(r"\d+\s+min\s+read$", "", cleaned, flags=re.IGNORECASE)
    cleaned = re.sub(r"[^\w\s'-]+", " ", cleaned)
    cleaned = re.sub(r"\s+", " ", cleaned).strip().lower()
    return cleaned


def clean_price(price_text: str) -> float | None:
    """Extract a float from a price string while preserving the sign."""
    normalized = price_text.strip().replace(",", "")
    if not normalized:
        return None

    match = re.search(r"-?\d+(?:\.\d+)?", normalized)
    if match is None:
        return None

    return float(match.group(0))
