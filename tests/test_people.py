import pytest
from people.py import load_people
from datetime import date

def test_load_people_default():
    assert load_people(r"peer_finder\tests\test_data\default.csv") == {"id": 1001, "name": "Anna Keller", "birthdate": date(2001, 9, 14)}

def test_load_people_invalid_id():
    with pytest.raises(ValueError):
        load_people(r"peer_finder\tests\test_data\invalid_id.csv")

def test_load_people_empy_space():
    with pytest.raises(ValueError):
        load_people(r"peer_finder\tests\test_data\empty_space.csv")

def test_duplicate_id_raises_value_error():
    with pytest.raises(ValueError):
        load_people(r"peer_finder\tests\test_data\duplicate_id.csv")