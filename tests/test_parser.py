from pathlib import Path

from wsj_scraper.parser import parse_dollar_index_price, parse_headlines


FIXTURES = Path(__file__).parent / "fixtures"


def test_parse_headlines_returns_clean_deduplicated_results() -> None:
    html = (FIXTURES / "wsj_homepage.html").read_text()

    assert parse_headlines(html) == [
        "stocks rally as inflation fears ease",
        "tech giants beat expectations",
        "dollar falls as traders weigh tariffs",
    ]


def test_parse_dollar_index_price_reads_quote_value() -> None:
    html = (FIXTURES / "wsj_market_data.html").read_text()

    assert parse_dollar_index_price(html) == 105.42
