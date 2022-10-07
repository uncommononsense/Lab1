def MergeSubSeq(arr, l, r, end, temp):
    
    x = l
    y = r
    m = 0
    
    while x < r and y < end:
        if arr[x] < arr[y] :
            temp[m] = arr[x]
            x += 1
        else :
            temp[m] = arr[y]
            y += 1
            
        m += 1
        
    while x < r :
        temp[m] = arr[x]
        x += 1
        m += 1
        
    while y < end:
        temp[m] = arr[y]
        y += 1
        m += 1

    for i in range(end - l):
        
        arr[i + l] = temp[i]

def MergeRecSort(arr, f, l, temp):
    if f == l:
        return
    else :
        m = (f + l) // 2
    MergeRecSort(arr, first, mid, temp)
    MergeRecSort(arr, mid+1, last, temp)
    MergeSubSeq(arr, first, mid+1, last+1, temp)

def MergeSort(arr): 
    l = len(arr)
    temp = [-1] * l
    MergeRecSort(arr, 0, n-1, temp)
    return temp
