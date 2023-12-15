# returns the sum of a list recursively, inside both head-tail and divide and conquer algorithms.

def head_tail_sum(array: list[int]) -> int:
    if len(array) == 1:
        return array[0]
    elif len(array) == 0:
        return 0

    head, tail = array[0], array[1:]
    return head + head_tail_sum(tail)


def dc_sum(array: list[int]) -> int:
    if len(array) == 1:
        return array[0]
    elif len(array) == 0:
        return 0

    mid = len(array) // 2
    front, back = array[:mid], array[mid:]

    return dc_sum(front) + dc_sum(back)    


