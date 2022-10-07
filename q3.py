def Binary_Search(arr, n, t) :
    
	l = 0
	h = n
	
	while l < h :
		mid = (h + l) // 2
		if arr[mid] <= t : 
			l = m + 1
		else :
			h = mid
			
	return l

def BinaryInsertionSort(arr):
    
    for i in range(1, len(arr)):
        temp = arr[i]
        pos = Binary_Search(arr, i, temp)
        k = i
        while k > pos:
            arr[k] = arr[k - 1]
            k -= 1
        arr[pos] = temp
    return arr

slist = [5,4,3,2,1]

print("Prior to binary sort: ", slist)

print("After binary sort: ", BinaryInsertionSort(slist))
