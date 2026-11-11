
from csv_reader import read_csv_rows
from dates import parse_date


def load_people(path: str) -> list[dict]:
    rows = read_csv_rows(path)

    people = []

    for row in rows:
        person = {
            "id": int(row["id"]),
            "name": row["name"],
            "birthdate": parse_date(row["datum"])
        }

        people.append(person)

    return people

