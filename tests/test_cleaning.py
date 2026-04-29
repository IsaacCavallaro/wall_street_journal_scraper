from wsj_scraper.cleaning import clean_headline, clean_price


def test_clean_headline_normalizes_noise() -> None:
    headline = "Breaking News [Updated]: Dollar Falls (Live Updates) 5 min read"

    assert clean_headline(headline) == "breaking news dollar falls"


def test_clean_price_extracts_signed_floats() -> None:
    assert clean_price("$105.42") == 105.42
    assert clean_price("-90.10") == -90.10
    assert clean_price("N/A") is None
