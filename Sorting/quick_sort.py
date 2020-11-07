def partition(arr, left, right):
    pivot = arr[(left+right)//2]
    
    # All elements less then pivot comes before elements bigger than pivot
    while left<=right:
        while arr[left]<pivot:
            left+=1
        while arr[right]>pivot:
            right-=1
        
        if left<=right:
            arr[left], arr[right] = arr[right], arr[left]
            left+=1
            right-=1
    return left

def quick_sort(arr, left=None, right=None):
    if left==None and right==None:
        left = 0
        right = len(arr)-1
    if left >= right:
        return
    
    partition_index = partition(arr, left, right)
    quick_sort(arr, left = left, right = partition_index-1)
    quick_sort(arr, left = partition_index, right = right)

if __name__ == "__main__":
    arr = [1, 2, 0, 10, 5, 0, -1, -100, 19, 10, 0]
    quick_sort(arr)
    print("Using Quick Sort : ", arr) 