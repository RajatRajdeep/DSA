def insertion_sort(arr):
    for i in range(1, len(arr)):       
        val = arr[i]
        j = i-1
        while val<arr[j] and j>=0:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = val
    return arr

if __name__ == "__main__":
    arr = [1, 2, 0, 10, 5, 0, -1, -100, 19, 10, 0]
    print("Using Insertion Sort : ", insertion_sort(arr))