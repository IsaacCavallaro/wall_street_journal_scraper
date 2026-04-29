from pathlib import Path

from wsj_scraper.client import WSJScraper
from wsj_scraper.models import ScrapeConfig


FIXTURES = Path(__file__).parent / "fixtures"


class StubResponse:
    def __init__(self, text: str, status_code: int = 200) -> None:
        self.text = text
        self.status_code = status_code

    def raise_for_status(self) -> None:
        if self.status_code >= 400:
            raise RuntimeError("boom")


class StubSession:
    def __init__(self) -> None:
        self.calls: list[str] = []
        self.responses = {
            "https://www.wsj.com/": StubResponse((FIXTURES / "wsj_homepage.html").read_text()),
            "https://www.wsj.com/market-data/quotes/index/DXY": StubResponse(
                (FIXTURES / "wsj_market_data.html").read_text()
            ),
        }

    def get(self, url: str, headers: dict[str, str], timeout: float) -> StubResponse:
        self.calls.append(url)
        assert "User-Agent" in headers
        assert timeout == 5.0
        return self.responses[url]


def test_scrape_returns_snapshot_from_session() -> None:
    session = StubSession()
    scraper = WSJScraper(
        config=ScrapeConfig(timeout_seconds=5.0),
        session=session,
    )

    result = scraper.scrape()

    assert result is not None
    assert result.dollar_index_price == 105.42
    assert len(result.headlines) == 3
    assert session.calls == [
        "https://www.wsj.com/",
        "https://www.wsj.com/market-data/quotes/index/DXY",
    ]
