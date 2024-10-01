def BinarySearch(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return mid

        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1


search = BinarySearch([1, 4, 5, 8, 11, 14, 16], 14)

print(search)