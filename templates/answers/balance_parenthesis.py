def balance_parenthesis(pairs: int, open_rem=None, close_rem=None, current='') -> list[str]:
    if open_rem is None:
        open_rem = pairs
    if close_rem is None:
        close_rem = pairs

    if open_rem == 0 and close_rem == 0:
        return [current]

    results = []

    if open_rem > 0:
        results.extend(balance_parenthesis(pairs, open_rem - 1, close_rem, current + '('))
    if close_rem > open_rem:
        results.extend(balance_parenthesis(pairs, open_rem, close_rem - 1, current + ')'))

    return results 