
arr = [2,5,10]


def profArray(arr, p, l):

    if l > 2:
        print(p)
        return p
    
    p = p*arr[l]
    
    return profArray(arr, p, l+1)

p = 1
l = 0
profArray(arr, p, l)
        
