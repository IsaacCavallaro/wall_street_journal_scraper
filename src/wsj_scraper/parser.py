from __future__ import annotations

from bs4 import BeautifulSoup

from .cleaning import clean_headline, clean_price


HEADLINE_SELECTORS = (
    "article h3 a",
    "article h2 a",
    "[class*='headline'] a",
    "[class*='headline']",
    "h3[class*='headline']",
)

PRICE_SELECTORS = (
    "#quote_val",
    "[data-testid='quote-value']",
    "[class*='quote_val']",
    "[class*='price']",
    "[class*='value']",
)


def parse_headlines(html: str) -> list[str]:
    """Parse and normalize likely headline nodes from a WSJ-like page."""
    soup = BeautifulSoup(html, "html.parser")
    headlines: list[str] = []
    seen: set[str] = set()

    for selector in HEADLINE_SELECTORS:
        for node in soup.select(selector):
            text = node.get_text(" ", strip=True)
            if not text:
                continue

            cleaned = clean_headline(text)
            if len(cleaned) < 12 or cleaned in seen:
                continue

            seen.add(cleaned)
            headlines.append(cleaned)

    return headlines


def parse_dollar_index_price(html: str) -> float | None:
    """Parse the DXY quote from a WSJ market-data page."""
    soup = BeautifulSoup(html, "html.parser")

    for selector in PRICE_SELECTORS:
        node = soup.select_one(selector)
        if node is None:
            continue

        price = clean_price(node.get_text(" ", strip=True))
        if price is not None:
            return price

    return None
