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