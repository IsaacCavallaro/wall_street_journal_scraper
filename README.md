# Wall Street Journal Scraper

`wall_street_journal_scraper` is a small Python CLI that captures a Wall Street Journal snapshot:

- current DXY quote from WSJ market data
- normalized WSJ homepage headlines
- a simple lexical signal summary over the captured headlines

The original repo had the right idea but was not production-grade: the package layout was broken, tests hit live network endpoints, and large parts of the project were dead scaffolding. This version keeps the same core idea and modernizes it into a repo that is installable, testable, and easier to extend.

## Stack

- Python 3.11+
- `requests`
- `beautifulsoup4`
- `pytest`
- `hatchling` via `pyproject.toml`

## Quick Start

Create a virtual environment and install the project in editable mode:

```bash
env -u HTTP_PROXY -u HTTPS_PROXY -u http_proxy -u https_proxy python3 -m venv .venv
source .venv/bin/activate
env -u HTTP_PROXY -u HTTPS_PROXY -u http_proxy -u https_proxy python -m pip install --upgrade pip
env -u HTTP_PROXY -u HTTPS_PROXY -u http_proxy -u https_proxy pip install -e ".[dev]"
```

Run the CLI:

```bash
wsj-scraper
```

For JSON output:

```bash
wsj-scraper --format json
```

## Development

Run tests:

```bash
pytest
```

The test suite uses HTML fixtures under `tests/fixtures/` and does not call WSJ live.

## Package Layout

```text
src/wsj_scraper/
  analysis.py
  cleaning.py
  cli.py
  client.py
  models.py
  parser.py
tests/
  fixtures/
```

## Notes

- Scraping public websites can break when markup changes. The parser is written with fallback selectors, but it is still dependent on WSJ HTML structure.
- WSJ currently serves anti-bot responses to many unauthenticated requests. When that happens, the CLI exits with a descriptive fetch error instead of silently returning empty data.
- The signal analysis is intentionally lightweight. It is a quick lexical snapshot, not a rigorous macroeconomic model.
- If you want persistence later, add it as a separate module once the collection pipeline is stable.
