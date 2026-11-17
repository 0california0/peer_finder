import pytest
from datetime import date
from birthday_projekt.analysis import find_age_neighbors
from birthday_projekt.analysis import find_birthday_groups

# find_age_neighbours

def test_find_age_neighbors_default():
    people = [
        {"id": 1, "name": "person_1", "birthdate": date(2001, 1, 1)},
        {"id": 2, "name": "person_2", "birthdate": date(2001, 1, 2)},
        {"id": 3, "name": "person_3", "birthdate": date(2001, 1, 10)},
        {"id": 4, "name": "person_4", "birthdate": date(2001, 1, 25)}
    ]

    assert find_age_neighbors(people)[1] == [2, 3, 4]

def test_find_age_neighbors_different_year():
    people = [
        {"id": 1, "name": "person_1", "birthdate": date(2001, 1, 10)},
        {"id": 2, "name": "person_2", "birthdate": date(2002, 1, 10)},
        {"id": 3, "name": "person_3", "birthdate": date(2001, 1, 20)}
    ]

    assert find_age_neighbors(people)[1] == [3, 2]

def test_find_age_neighbors_smaller_id():
    people = [
            {"id": 1, "name": "person_1", "birthdate": date(2001, 1, 10)},
            {"id": 2, "name": "person_2", "birthdate": date(2001, 1, 11)},
            {"id": 3, "name": "person_3", "birthdate": date(2001, 1, 9)}
        ]
    assert find_age_neighbors(people)[1] == [2, 3]

def test_find_age_neighbors_n():
    people = [
            {"id": 1, "name": "person_1", "birthdate": date(2001, 1, 1)},
            {"id": 2, "name": "person_2", "birthdate": date(2001, 2, 1)},
            {"id": 3, "name": "person_3", "birthdate": date(2001, 3, 1)},
            {"id": 4, "name": "person_4", "birthdate": date(2001, 4, 1)},
            {"id": 5, "name": "person_5", "birthdate": date(2001, 5, 1)},
            {"id": 6, "name": "person_6", "birthdate": date(2001, 6, 1)},
            {"id": 7, "name": "person_7", "birthdate": date(2001, 7, 1)},
            {"id": 8, "name": "person_8", "birthdate": date(2001, 8, 1)},
            {"id": 9, "name": "person_9", "birthdate": date(2001, 9, 1)},
            {"id": 10, "name": "person_10", "birthdate": date(2001, 10, 1)},
            {"id": 11, "name": "person_11", "birthdate": date(2001, 11, 1)},
            {"id": 12, "name": "person_12", "birthdate": date(2001, 12, 1)},
        ]
    assert find_age_neighbors(people)[6] == [7, 5, 4, 8, 3, 9, 2, 10, 1, 11]

    assert find_age_neighbors(people, n=20)[6] == [7, 5, 4, 8, 3, 9, 2, 10, 1, 11]

    assert find_age_neighbors(people, n=3)[6] == [7, 5, 4]

    assert find_age_neighbors(people, n=0)[6] == []

# find_birthday_groups

def test_find_birthday_groups_default():
    people = [
                {"id": 1, "name": "person_1", "birthdate": date(2001, 1, 1)},
                {"id": 2, "name": "person_2", "birthdate": date(2002, 1, 1)},
                {"id": 3, "name": "person_3", "birthdate": date(2001, 6, 1)},
                {"id": 4, "name": "person_4", "birthdate": date(2001, 4, 1)},
                {"id": 5, "name": "person_5", "birthdate": date(2001, 1, 1)},
                {"id": 6, "name": "person_6", "birthdate": date(2001, 6, 1)},
            ]
    assert find_birthday_groups(people) == {
        (1, 1) : [1, 2, 5],
        (6, 1) : [3, 6],
        (4, 1) : [4]
    }

def test_find_birthday_groups_switched_date():
    people = [
                    {"id": 1, "name": "person_1", "birthdate": date(2001, 1, 2)},
                    {"id": 2, "name": "person_2", "birthdate": date(2002, 2, 1)},
            ]
    assert find_birthday_groups(people) == {
        (1, 2) : [1],
        (2, 1) : [2]
    }

def test_find_birthday_groups_leap_year():
    people = [
                        {"id": 1, "name": "person_1", "birthdate": date(2001, 2, 29)},
                        {"id": 2, "name": "person_2", "birthdate": date(2002, 2, 29)},
            ]
    assert find_birthday_groups(people) == {(2, 29) : [1, 2]}