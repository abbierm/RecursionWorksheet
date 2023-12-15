# Function that sorts a list recursively with merge sort algorithm

def merge_sort(array: list[int]) -> list[int]:
    if len(array) == 0 or len(array) == 1:
        return array
    
    mid = len(array) // 2
    left, right = merge_sort(array[:mid]), merge_sort(array[mid:])

    l, r = 0, 0
    results = []

    while len(results) < len(array):
        if left[l] < right[r]:
            results.append(left[l])
            l += 1
        else:
            results.append(right[r])
            r += 1
        
        if l == len(left):
            results.extend(right[r:])
            break
        elif r == len(right):
            results.extend(left[l:])
            break
    
    return results