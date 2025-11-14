# lists the different ordering of items in a list without repeats

def get_list_permutations(array: list) -> list[list]:
    if len(array) == 1:
        return [array]

    results = []
    for item in array:
        rest_array = [thing for thing in array if thing != item]

        rest_permutations = get_list_permutations(rest_array)
        for rest_perm in rest_permutations:
            new = [item] + rest_perm
            results.append(new)

    return results


