
def print_permutations(arry: list, k: int | None = None):
    """
        This is heap's algorithm
        https://en.wikipedia.org/wiki/Heap%27s_algorithm
    """
    if k is None:
        k = len(arry)
    if k == 1:
        print(arry)
        return
    for i in range(k):
        print_permutations(arry, k - 1)
        if k % 2 == 0:
            arry[i], arry[k - 1] = arry[k - 1], arry[i]
        else:
            arry[0], arry[k - 1] = arry[k - 1], arry[0]



print_permutations([1, 2, 3])