def SelectionSort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j

        if min_index != i:
            temp = arr[i]
            arr[i] = min_index
            arr[min_index] = temp

    return arr


sort = SelectionSort([45, 1, 8, 20, 9])

print(sort)