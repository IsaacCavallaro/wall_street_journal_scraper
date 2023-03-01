import requests
from bs4 import BeautifulSoup
import re


class WSJScraper:
    def __init__(self, url, headers):
        self.url = url
        self.headers = headers

    def _get_html(self, url):
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            html = response.text
            return html
        else:
            return None

    def _get_price(self, soup):
        price_tag = soup.select_one('#quote_val')
        if price_tag is not None:
            price_str = price_tag.text.strip()
            if price_str is not None:
                price = float(price_str)
                return price
        return None


    def _get_headlines(self, soup):
        headlines = []
        headline_tags = soup.select('.WSJTheme--headline--7VCzo7Ay')
        for tag in headline_tags:
            headline = tag.text.strip()
            if headline:
                headlines.append(headline)
        return headlines

    def scrape(self):
        headlines_url = self.url
        dollar_price_url = 'https://www.wsj.com/market-data/quotes/index/DXY'

        headlines_html = self._get_html(headlines_url)
        if headlines_html is not None:
            headlines_soup = BeautifulSoup(headlines_html, 'html.parser')
            try:
                headlines = self._get_headlines(headlines_soup)
            except Exception:
                return None
        else:
            return None

        dollar_price_html = self._get_html(dollar_price_url)
        if dollar_price_html is not None:
            dollar_price_soup = BeautifulSoup(dollar_price_html, 'html.parser')
            try:
                price = self._get_price(dollar_price_soup)
            except Exception:
                return None
        else:
            return None

        return {'price': price, 'headlines': headlines}


def main():
    url = "https://www.wsj.com/"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    scraper = WSJScraper(url, headers)
    result = scraper.scrape()
    if result is not None:
        dollar_price = result['price']
        headlines = result['headlines']
        print(f"Dollar price: {dollar_price}")
        print(f"Headlines: {headlines}")
    else:
        print("Scraping failed.")


if __name__ == "__main__":
    main()
