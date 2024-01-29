def quick_sort(array: list[int], left=None, right=None) -> list[int]:
    if left is None:
        left = 0
    if right is None:
        right = len(array) - 1

    if right <= left:
        return

    i = left
    pivot = array[right]
 
    for j in range(left, right):
        if array[j] <= pivot:
            array[i], array[j] = array[j], array[i]
            i += 1

    array[i], array[right] = array[right], array[i]

    quick_sort(array, left, i - 1)
    quick_sort(array, i + 1, right)