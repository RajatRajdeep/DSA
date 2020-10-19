arr = list(range(0, 10))

def binary_search(arr, val):
    low = 0
    high = len(arr)-1

    while low<=high:
        mid = (low+high)//2
        if arr[mid] == val:
            return mid
        elif arr[mid] > val:
            high = mid-1
        else:
            low = mid+1
    return -1

def recursive_binary_search(arr, low, high, val):
    if low>high:
        return -1

    mid = (low+high)//2
    if arr[mid] == val:
        return mid
    elif arr[mid] > val:
        return recursive_binary_search(arr, low, mid-1, val)
    else:
        return recursive_binary_search(arr, mid+1, high, val)

if __name__ == "__main__":
    import sys
    print("Using While Loop : ", binary_search(arr, int(sys.argv[1])))
    print("Using Recursive Function : ", recursive_binary_search(arr, 0, len(arr)-1, int(sys.argv[1])))