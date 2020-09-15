def linear_search(arr, target):
    position = 0
    while position < len(arr):
        if arr[position] == target:
            return position
        else:
            position = position + 1

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    low = 0
    length = len(arr) - 1

    while low <= length:
        mid = (length + low) // 2

        if arr[mid] < target:
            low = mid + 1
        elif arr[mid] > target:
            length = mid - 1
        else:
            return mid

    return -1  # not found
