def CountingSort(arr, val):
    
    l = len(arr)
    
    output = [0]*l
    con = [0]*(10)
    
    for i in range(0, l):
        k = (arr[i] / val)
        con[int((k) % 10)] += 1

    for i in range(1,10):
        con[i] += con[i - 1]

    for i in range(n - 1, -1, -1):
        k = (arr[i] / val)
        output[con[int((k) % 10) ] - 1] = arr[i]
        con[int((k) % 10)] -= 1

    for i in range(0,len(arr)):
        arr[i] = output[i]

def RadixSort(arr):
    
    MaxEle = max(arr)
    
    exp = 1
    
    while MaxEle/exp > 0:
        
        CountingSort(arr,exp)
        exp *= 10
        
    return arr
