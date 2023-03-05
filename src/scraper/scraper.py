# pylint: disable=missing-module-docstring, missing-class-docstring, missing-function-docstring, too-few-public-methods
import requests
from bs4 import BeautifulSoup


class WSJScraper:
    def __init__(self, url, headers):
        self.url = url
        self.headers = headers

    def _get_html(self, url):
        try:
            response = requests.get(url, headers=self.headers, timeout=10)
            response.raise_for_status()  # raise an error if status code is not 200
            html = response.text
            return html
        except (requests.exceptions.HTTPError, requests.exceptions.RequestException):
            return None

    def _get_price(self, soup):
        try:
            price_tag = soup.select_one("#quote_val")
            if price_tag is not None:
                price_str = price_tag.text.strip()
                if price_str is not None:
                    price = float(price_str)
                    return price
        except (AttributeError, ValueError):
            pass
        return None

    def _get_headlines(self, soup):
        headlines = []
        try:
            headline_tags = soup.select(".WSJTheme--headline--7VCzo7Ay")
            for tag in headline_tags:
                headline = tag.text.strip()
                if headline:
                    headlines.append(headline)
        except (AttributeError, ValueError):
            pass

        return headlines

    def scrape(self):
        headlines_url = self.url
        dollar_price_url = "https://www.wsj.com/market-data/quotes/index/DXY"

        headlines_html = self._get_html(headlines_url)

        if headlines_html is not None:
            headlines_soup = BeautifulSoup(headlines_html, "html.parser")
            try:
                headlines = self._get_headlines(headlines_soup)
            except (AttributeError, ValueError):
                return None
        else:
            return None

        dollar_price_html = self._get_html(dollar_price_url)

        if dollar_price_html is not None:
            dollar_price_soup = BeautifulSoup(dollar_price_html, "html.parser")
            try:
                price = self._get_price(dollar_price_soup)
            except (AttributeError, ValueError):
                return None
        else:
            return None

        return {"price": price, "headlines": headlines}


def main():
    url = "https://www.wsj.com/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/58.0.3029.110 Safari/537.3"
    }

    scraper = WSJScraper(url, headers)
    result = scraper.scrape()
    if result is not None:
        dollar_price = result["price"]
        headlines = result["headlines"]
        if dollar_price is not None:
            print(f"Dollar price: {dollar_price}")
        else:
            print("Unable to retrieve dollar price.")
        if headlines:
            print(f"Headlines: {headlines}")
        else:
            print("Unable to retrieve headlines.")
    else:
        print("Scraping failed.")


if __name__ == "__main__":
    main()
