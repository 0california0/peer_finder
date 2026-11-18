from collections import defaultdict

def find_age_neighbors(people, n=10):
    neighbors = {}

    for first_person in people:
        pairs = []
        for second_person in people:
            if second_person['id'] == first_person['id']:
                continue
        age_distance = abs((first_person["birthdate"] - second_person["birthdate"]).days)
        pairs.append((age_distance, second_person["id"]))
        pairs.sort()

        ids = []
        for age_distance, second_person_id in pairs[:n]:
            ids.append(second_person_id)
        neighbors[first_person['id']] = ids

    return neighbors


def find_birthday_groups(people): 
    birthday_groups = defaultdict(list)

    for person in people:
        birthdate = person["birthdate"]
        birthday_key = (birthdate.month, birthdate.day)
        birthday_groups[birthday_key].append(person["id"])

    groups = {}
    for birthday, ids in birthday_groups.items():
        if len(ids) > 1:
            groups[birthday] = sorted(ids)

    return groups