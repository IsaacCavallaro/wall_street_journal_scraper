from wsj_scraper import cli
from wsj_scraper.models import ScrapeResult


class StubScraper:
    def scrape(self) -> ScrapeResult:
        return ScrapeResult(
            dollar_index_price=105.42,
            headlines=["stocks rally as inflation fears ease"],
            homepage_url="https://www.wsj.com/",
            market_url="https://www.wsj.com/market-data/quotes/index/DXY",
        )


def test_render_text_contains_summary() -> None:
    payload = {
        "result": {
            "dollar_index_price": 105.42,
            "headlines": ["stocks rally as inflation fears ease"],
        },
        "analysis": {
            "headline_analysis": {
                "total_headlines": 1,
                "dominant_signal": "bullish",
                "sentiment_score": 1.0,
            }
        },
    }

    rendered = cli.render_text(payload)

    assert "WSJ Snapshot" in rendered
    assert "DXY: 105.42" in rendered
    assert "- stocks rally as inflation fears ease" in rendered
