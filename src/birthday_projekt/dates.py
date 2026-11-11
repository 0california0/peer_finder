
from datetime import date, datetime

def parse_date(text: str) -> date:
    try:
        return date.fromisoformat(text)
    except ValueError:
        return datetime.strptime(text, "%d.%m.%Y").date()

