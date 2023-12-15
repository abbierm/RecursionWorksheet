# Finds all the possible orderings of a string that set length with repeats.
# Strings can 

def string_permutations(chars: str, length=None, current=''):
    if length is None:
        length = length(chars)
    if length == 0:
        return [current]

    results = []
    for char in chars:
        new = current + char
        results.extend(string_permutations(chars, length - 1, new))
    return results
