import pytest
from src.data.clean_data import clean_headline, clean_price


@pytest.mark.parametrize(
    "headline, expected",
    [
        (
            "Breaking News: Apple Unveils New Products",
            "breaking news apple unveils new products",
        ),
        (
            "Breaking News (Updated): Apple Unveils New Products",
            "breaking news apple unveils new products",
        ),
        (
            "Breaking News [Updated]: Apple Unveils New Products",
            "breaking news apple unveils new products",
        ),
        (
            "Breaking News:   Apple Unveils New Products  ",
            "breaking news apple unveils new products",
        ),
        (
            "Breaking News: $Apple Unveils New Products",
            "breaking news apple unveils new products",
        ),
    ],
)
def test_clean_headline(headline, expected):
    assert clean_headline(headline) == expected


@pytest.mark.parametrize(
    "price_str, expected",
    [
        ("90.10", 90.10),
        ("$90.10", 90.10),
        ("-$90.10", -90.10),
        ("90", 90),
        ("$90", 90),
        ("-90", -90),
        ("N/A", None),
        ("--", None),
        ("", None),
    ],
)
def test_clean_price(price_str, expected):
    assert clean_price(price_str) == expected
