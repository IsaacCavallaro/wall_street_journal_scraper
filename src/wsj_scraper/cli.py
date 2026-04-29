from __future__ import annotations

import argparse
import json
from dataclasses import asdict

from .analysis import analyze_snapshot
from .client import ScrapeError, WSJScraper
from .models import ScrapeConfig


def build_parser() -> argparse.ArgumentParser:
    defaults = ScrapeConfig()
    parser = argparse.ArgumentParser(
        prog="wsj-scraper",
        description="Scrape WSJ headlines and the DXY quote, then print a compact analysis.",
    )
    parser.add_argument("--homepage-url", default=defaults.homepage_url)
    parser.add_argument("--market-url", default=defaults.market_url)
    parser.add_argument("--timeout", type=float, default=defaults.timeout_seconds)
    parser.add_argument("--format", choices=("text", "json"), default="text")
    return parser


def render_text(payload: dict[str, object]) -> str:
    result = payload["result"]
    analysis = payload["analysis"]["headline_analysis"]
    headlines = result["headlines"]
    lines = [
        "WSJ Snapshot",
        f"DXY: {result['dollar_index_price'] if result['dollar_index_price'] is not None else 'unavailable'}",
        f"Headlines captured: {analysis['total_headlines']}",
        f"Dominant signal: {analysis['dominant_signal']} ({analysis['sentiment_score']})",
    ]
    if headlines:
        lines.append("Top headlines:")
        lines.extend(f"- {headline}" for headline in headlines[:5])
    return "\n".join(lines)


def main() -> int:
    args = build_parser().parse_args()
    config = ScrapeConfig(
        homepage_url=args.homepage_url,
        market_url=args.market_url,
        timeout_seconds=args.timeout,
    )
    scraper = WSJScraper(config=config)
    try:
        result = scraper.scrape()
    except ScrapeError as exc:
        print(f"Scraping failed: {exc}")
        return 1

    analysis = analyze_snapshot(result)
    payload = {
        "result": asdict(result),
        "analysis": asdict(analysis),
    }

    if args.format == "json":
        print(json.dumps(payload, indent=2))
    else:
        print(render_text(payload))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
