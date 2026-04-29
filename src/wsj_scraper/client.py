from __future__ import annotations

from dataclasses import replace

import requests

from .models import ScrapeConfig, ScrapeResult
from .parser import parse_dollar_index_price, parse_headlines


class ScrapeError(RuntimeError):
    """Raised when the remote source cannot be fetched or parsed."""


class WSJScraper:
    """Client for collecting a headline snapshot and DXY price."""

    def __init__(
        self,
        config: ScrapeConfig | None = None,
        session: requests.Session | None = None,
    ) -> None:
        self.config = config or ScrapeConfig()
        self.session = session or requests.Session()

    def fetch_html(self, url: str) -> str | None:
        try:
            response = self.session.get(
                url,
                headers=self.config.headers,
                timeout=self.config.timeout_seconds,
            )
            response.raise_for_status()
        except requests.HTTPError as exc:
            status_code = exc.response.status_code if exc.response is not None else "unknown"
            raise ScrapeError(f"WSJ returned HTTP {status_code} for {url}.") from exc
        except requests.RequestException as exc:
            raise ScrapeError(f"Request failed for {url}: {exc}") from exc

        return response.text

    def scrape(self) -> ScrapeResult:
        homepage_html = self.fetch_html(self.config.homepage_url)
        market_html = self.fetch_html(self.config.market_url)

        return ScrapeResult(
            dollar_index_price=parse_dollar_index_price(market_html),
            headlines=parse_headlines(homepage_html),
            homepage_url=self.config.homepage_url,
            market_url=self.config.market_url,
        )

    def with_config(self, **changes: object) -> "WSJScraper":
        return WSJScraper(config=replace(self.config, **changes), session=self.session)
