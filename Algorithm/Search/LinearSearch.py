def LinearSearch(arr, n):
    for i in range(len(arr)):
        if arr[i] == n:
            return i

    return -1


search = LinearSearch([45, 14, 2, 8], 8)

print("Found element in index ", search)
