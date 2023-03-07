import re


def clean_headline(headline):
    # Remove any characters inside parentheses AND brackets
    headline = re.sub(r"\([^)]*\)", "", headline)
    headline = re.sub(r"\[[^]]*\]", "", headline)

    headline = headline.strip()

    # Remove any leading/trailing punctuation marks
    headline = re.sub(r"^\W+|\W+$", "", headline)

    # Replace any remaining whitespace with a single space character
    headline = re.sub(r"\s+", " ", headline)
    headline = headline.lower()

    # Remove trailing 'X min read' statements
    cleaned_headline = re.sub(r"\d+ min read$", "", headline)

    return cleaned_headline


def clean_price(price_str):
    # Remove any non-digit characters from price string
    price = re.sub(r"[^\d.]", "", price_str)

    try:
        price = float(price)
    except ValueError:
        return None

    return price
