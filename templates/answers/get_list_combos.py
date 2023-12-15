def get_list_combos(array: list, k: int) -> list[list]:
    if k == 0:
        return [[]]
    if len(array) == 0:
        return []

    results = []
    head, rest = array[:1], array[1:]

    rest_combos = get_list_combos(rest, k - 1)
    for combo in rest_combos:
        results.append(head + combo)
    results.extend(get_list_combos(rest, k))
    return results
