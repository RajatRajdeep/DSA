def selection_sort(arr):
    for i in range(0, len(arr)-1):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[min_index]>arr[j]:
                min_index = j
        arr[min_index], arr[i] = arr[i], arr[min_index]
    return arr

if __name__ == "__main__":
    arr = [1, 2, 0, 10, 5, 0, -1, -100, 19, 10, 0]
    print("Using Selection Sort : ", selection_sort(arr))