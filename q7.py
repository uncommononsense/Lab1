import random

def Part(a,l,r):
    
    pivot = a[l]
    i = l + 1
    
    for j in range(l + 1, r):
        
        if a[j] < pivot:
            a[j], a[i] = a[i], a[j]
            i += 1
            
    a[l], a[i - 1] = a[i - 1],a[l]
    
    return i - 1

def QuickSortRandom(arr, lef, rig):
    
    if lef  <  rig:
        
        pivot = random.randint(lef, rig - 1)
        arr[pivot], arr[lef] = arr[lef], arr[pivot]
        pivot_index = Part(arr, lef, rig)
        
        QuickSortRandom(arr, lef, pivot_index)
        QuickSortRandom(arr, pivot_index + 1, rig)
        
    return arr
