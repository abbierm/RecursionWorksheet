def get_string_combos(chars: str, k: int) -> list[str]:
    if k == 0:
        return ['']
    if len(chars) == 0:
        return []

    results = []
    head, rest = chars[0:1], chars[1:]
    rest_combos = get_string_combos(rest, k - 1)
    for rest_combo in rest_combos:
        results.append(head + rest_combo)
    results.extend(get_string_combos(rest, k))
    return results