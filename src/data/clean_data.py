import re


def clean_headline(headline):
    # Remove any characters inside parentheses and brackets
    headline = re.sub(r"\([^)]*\)", "", headline)
    headline = re.sub(r"\[[^]]*\]", "", headline)

    headline = headline.strip()

    # Remove any leading/trailing punctuation marks
    headline = re.sub(r"^\W+|\W+$", "", headline)

    # Replace any remaining whitespace with a single space character
    headline = re.sub(r"\s+", " ", headline)
    headline = headline.lower()

    return headline
