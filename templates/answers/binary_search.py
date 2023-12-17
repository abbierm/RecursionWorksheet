def binary_search(item: int, array: list, left=None, right=None):
    if left is None:
        left = 0
    if right is None:
        right = len(array) - 1
    if left > right:
        return None

    mid = (left + right) // 2

    if item == array[mid]:
        return mid
    elif item < array[mid]:
        return binary_search(item, array, left, mid - 1)
    elif item > array[mid]:
        return binary_search(item, array, mid + 1, right)