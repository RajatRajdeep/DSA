def linear_search(arr, val):
    for i in range(0, len(arr)):
        if arr[i] == val:
            return i
    return -1

if __name__ == "__main__":
    import sys
    arr = list(range(10, 0, -1))
    print(linear_search(arr, int(sys.argv[1])))
