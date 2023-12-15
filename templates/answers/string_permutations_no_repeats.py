# Get string permutations without repeating characters

def get_string_permutations(chars: str) -> str:
    if len(chars) == 1:
        return chars
    
    results = []
    head, rest = chars[0:1], chars[1:]
    rest_permutations = get_string_permutations(rest)
    for rest_perm in rest_permutations:
        for i in range(len(rest_perm) + 1):
            new_perm = rest_perm[0:i] + head + rest_perm[i:]
            results.append(new_perm)
    return results