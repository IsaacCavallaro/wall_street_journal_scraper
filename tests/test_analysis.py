from wsj_scraper.analysis import analyze_headlines, analyze_snapshot
from wsj_scraper.models import ScrapeResult


def test_analyze_headlines_scores_sentiment() -> None:
    analysis = analyze_headlines(
        [
            "stocks rally as inflation fears ease",
            "tech giants beat expectations",
            "dollar falls as traders weigh tariffs",
        ]
    )

    assert analysis.total_headlines == 3
    assert analysis.bullish_matches == 1
    assert analysis.bearish_matches == 1
    assert analysis.neutral_matches == 1
    assert analysis.dominant_signal == "neutral"
    assert analysis.sentiment_score == 0.0


def test_analyze_snapshot_wraps_result() -> None:
    result = ScrapeResult(
        dollar_index_price=105.42,
        headlines=["stocks rally as inflation fears ease"],
        homepage_url="https://www.wsj.com/",
        market_url="https://www.wsj.com/market-data/quotes/index/DXY",
    )

    snapshot = analyze_snapshot(result)

    assert snapshot.dollar_index_price == 105.42
    assert snapshot.headline_analysis.total_headlines == 1
