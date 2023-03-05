import pytest
from src.scraper.scraper import WSJScraper


@pytest.fixture(scope="module")
def scraper():
    url = "https://www.wsj.com/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/58.0.3029.110 Safari/537.3"
    }
    return WSJScraper(url, headers)


def test_scrape_returns_dict(scraper):
    result = scraper.scrape()
    assert isinstance(result, dict)


def test_scrape_returns_price_and_headlines_keys(scraper):
    result = scraper.scrape()
    assert "price" in result
    assert "headlines" in result


def test_scrape_returns_nonempty_price_and_headlines_values(scraper):
    result = scraper.scrape()
    assert result["price"] is not None
    assert result["headlines"]


def test_scrape_with_invalid_url_returns_none(scraper):
    scraper.url = "https://www.invalidurl.com/"
    result = scraper.scrape()
    assert result is None
