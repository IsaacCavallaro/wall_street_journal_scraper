from __future__ import annotations

from dataclasses import dataclass, field


DEFAULT_USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/124.0.0.0 Safari/537.36"
)


@dataclass(frozen=True, slots=True)
class ScrapeConfig:
    homepage_url: str = "https://www.wsj.com/"
    market_url: str = "https://www.wsj.com/market-data/quotes/index/DXY"
    timeout_seconds: float = 10.0
    user_agent: str = DEFAULT_USER_AGENT

    @property
    def headers(self) -> dict[str, str]:
        return {"User-Agent": self.user_agent}


@dataclass(frozen=True, slots=True)
class ScrapeResult:
    dollar_index_price: float | None
    headlines: list[str] = field(default_factory=list)
    homepage_url: str = ""
    market_url: str = ""


@dataclass(frozen=True, slots=True)
class HeadlineAnalysis:
    total_headlines: int
    bullish_matches: int
    bearish_matches: int
    neutral_matches: int
    sentiment_score: float
    dominant_signal: str


@dataclass(frozen=True, slots=True)
class SnapshotAnalysis:
    dollar_index_price: float | None
    headline_analysis: HeadlineAnalysis
