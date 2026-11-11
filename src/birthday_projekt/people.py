
from datetime import date, datetime
from csv_reader import read_csv_rows


def parse_date(value: str) -> date:
    try:
        return date.fromisoformat(value)
    except ValueError:
        return datetime.strptime(value, "%d.%m.%Y").date()


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


people = load_people("data/people_start.csv")
