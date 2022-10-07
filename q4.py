import time

def SelectionSort(slist):
    
    start = time.time()
    
    l = len(slist)
    
    for i in range(l):
        mini = i
        for j in range(i + 1, l):
            if slist[mini] > slist[j]:
                mini = j
                
        if mini != i :
            temp = slist[i]
            slist[i] = slist[min]
            slist[mini] = temp
            
    print("After Selection Sort: ", slist)
    print("Timing for Selection Sort: ")
    end = time.time()
    print((end - start) * 10 ** 3, "ms")

def BinarySearch(arr, n, t) :
	l = 0
	h = n
	while l < h :
		m = (h + l) // 2
		if arr[m] <= t: 
			l = m + 1
		else :
			h = m
	return l

def binary_insertionsort(arr):
    
    start = time.time()
    
    for i in range(1, len(arr)):
        
        temp = arr[i]
        pos = BinarySearch(array, i, temp)
        k = i
        
        while k > pos:
            arr[k] = arr[k - 1]
            k -= 1
            
        arr[pos] = temp
        
    print("After Binary Insertion Sorting: ", arr)
    print("Timing for Insertion Sort through Binary Search: ")
    
    end = time.time()
    
    print((end - start) * 10 ** 3, "ms")

def InsertionSort(arr):
    
    start = time.time()
    
    for i in range(1, len(arr)):
        temp = arr[i]
        j = i-1
        
        while j >= 0 and temp < arr[j] :
                arr[j + 1] = arr[j]
                j -= 1
                
        arr[j + 1] = temp
        
    print("After Linear Insertion Sort: ", arr)
    print("Timing for Insertion Sort through Linear Search: ")
    
    end = time.time()
    
    print((end - start) * 10 ** 3, "ms")


print("1. ")
l4 = [5,4,3,2,1]
print("Selection Sort:")
print("Before Sorting: ", l4)
selection_sort(l4)
print()
l5 = [5,4,3,2,1]
print("Insertion Sort:")
print("Before Sorting: ", l5)
binary_insertionsort(l5)
print("\n2. ")
l6 = [5,4,3,2,1]
print("Insertion Sort through Binary Search:")
print("Before Sorting: ", l6)
binary_insertionsort(l5)
print()
l7 = [5,4,3,2,1]
print("Insertion Sort through Linear Search:")
print("Before Sorting: ", l7)
insertion_sort(l7)
