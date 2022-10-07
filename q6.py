def QuickSort(arr, l, h):
    
    
    right = h
    left = l
    pivot = arr[(l + h) //2]
    
    if l >= h:
        return
    while left <= right:
        
        while arr[left] < pivot:
            left += 1
            
        while arr[right] > pivot:
            right -= 1
            
        if left <= right:
            swap(arr, left, right)
            left += 1
            right -= 1
            
    QuickSort(arr, low, right)
    QuickSort(arr, left, high)
    return arr

def Swap(arr, x, y):
    
        temp = None
        temp = arr[x]
        
        arr[x] = arr[y]
        arr[y] = temp

