import pytest
from datetime import date
from birthday_projekt.dates import parse_date

def test_parse_date_both_formats():
    assert parse_date("2002-04-01") == parse_date("01.04.2002")

def test_parse_date_not_valid():
    with pytest.raises(ValueError):
        parse_date("32.12.2002")
        parse_date("13.13.2027")

def test_parse_date_default_with_zero():
    assert parse_date("01.01.2001") == date(2001, 1, 1)
    assert parse_date("1.1.2001") == date(2001, 1, 1)

def test_parse_date_leap_year():
    assert parse_date("28.02.2024") == date(2024, 2, 28)

def test_parse_date_valid_format():
    with pytest.raises(ValueError):
        parse_date("test")
        parse_date("02,02,2002")