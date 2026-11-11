import pytest
from dates.py import parse_date
from datetime import date

def test_parse_date_not_valid():
    with pytest.raises(ValueError):
        parse_date("32.12.2002")
        parse_date("13.13.2027")

def test_parse_date_default_with_zero():
    assert parse_date("01.01.2001") == date(2001, 1, 1)
    assert parse_date("1.1.2001") == date(2001, 1, 1)