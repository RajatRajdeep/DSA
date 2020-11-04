def merge(arr1, arr2):
    arr = []
    i = j = 0
    
    while i<len(arr1) and j<len(arr2):
        if arr1[i]>arr2[j]:
            arr.append(arr2[j])
            j+=1
        else:
            arr.append(arr1[i])
            i+=1
    
    while i<len(arr1):
        arr.append(arr1[i])
        i+=1

    while j<len(arr2):
        arr.append(arr2[j])
        j+=1

    return arr

def merge_sort(arr):
    if len(arr) == 1:
        return arr
    
    mid = len(arr)//2
    return merge(merge_sort(arr[:mid]), merge_sort(arr[mid:]))

if __name__ == "__main__":
    arr = [1, 2, 0, 10, 5, 0, -1, -100, 19, 10, 0]
    print("Using Merge Sort : ", merge_sort(arr))