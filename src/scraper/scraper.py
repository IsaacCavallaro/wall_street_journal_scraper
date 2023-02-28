import requests
from bs4 import BeautifulSoup


class WSJScraper:
    def __init__(self, url):
        self.url = url

    def _get_html(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            return response.text
        else:
            return None

    def _get_price(self, soup):
        price_tag = soup.select_one('.WSJBase--column--10-5-3nD2q5gH')
        if price_tag is not None:
            price_str = price_tag.text.strip()
            price = float(price_str.replace(',', ''))
            return price
        else:
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
        html = self._get_html()
        if html is not None:
            soup = BeautifulSoup(html, 'html.parser')
            price = self._get_price(soup)
            headlines = self._get_headlines(soup)
            return {'price': price, 'headlines': headlines}
        else:
            return None


def main():
    url = "https://www.wsj.com/"
    scraper = WSJScraper(url)
    result = scraper.scrape()
    dollar_price = result['price']
    headlines = result['headlines']
    print(f"Dollar price: {dollar_price}")
    print(f"Headlines: {headlines}")


if __name__ == "__main__":
    main()
