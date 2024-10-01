def BubbleSort(arr):
    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp

    return arr


sort = BubbleSort([10, 9, 0, 1, 3])

print(sort)
