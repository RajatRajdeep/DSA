def bubble_sort_optimized(arr):
    for i in range(0, len(arr)-1):
        swap_flag = False
        for j in range(0, len(arr)-i-1):
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swap_flag = True
        if swap_flag==False:
            break

    return arr

def bubble_sort(arr):
    for i in range(0, len(arr)-1):
        for j in range(0, len(arr)-i-1):
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr

if __name__ == "__main__":
    arr = [1, 2, 0, 10, 5, 0, -1, -100, 19, 10, 0]
    print("Using Bubble Sort : ", bubble_sort(arr))
    print("Using Optimized Bubble Sort : ", bubble_sort_optimized(arr))