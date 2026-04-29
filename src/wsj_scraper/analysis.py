from __future__ import annotations

from .models import HeadlineAnalysis, ScrapeResult, SnapshotAnalysis


BULLISH_KEYWORDS = {
    "growth",
    "gain",
    "gains",
    "surge",
    "record",
    "beat",
    "beats",
    "expand",
    "expands",
    "rally",
    "rallies",
}

BEARISH_KEYWORDS = {
    "fall",
    "falls",
    "drop",
    "drops",
    "slump",
    "slumps",
    "loss",
    "losses",
    "recession",
    "fear",
    "fears",
    "tariff",
    "tariffs",
}


def analyze_headlines(headlines: list[str]) -> HeadlineAnalysis:
    bullish = 0
    bearish = 0
    neutral = 0

    for headline in headlines:
        words = set(headline.split())
        bullish_matches = len(words & BULLISH_KEYWORDS)
        bearish_matches = len(words & BEARISH_KEYWORDS)

        if bullish_matches > bearish_matches:
            bullish += 1
        elif bearish_matches > bullish_matches:
            bearish += 1
        else:
            neutral += 1

    total = len(headlines)
    score = 0.0 if total == 0 else round((bullish - bearish) / total, 3)

    if score > 0:
        dominant = "bullish"
    elif score < 0:
        dominant = "bearish"
    else:
        dominant = "neutral"

    return HeadlineAnalysis(
        total_headlines=total,
        bullish_matches=bullish,
        bearish_matches=bearish,
        neutral_matches=neutral,
        sentiment_score=score,
        dominant_signal=dominant,
    )


def analyze_snapshot(result: ScrapeResult) -> SnapshotAnalysis:
    return SnapshotAnalysis(
        dollar_index_price=result.dollar_index_price,
        headline_analysis=analyze_headlines(result.headlines),
    )
