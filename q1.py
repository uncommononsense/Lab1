def bubblesort(slist):
    
    l = len(slist) - 1
    
    while l > 0:
        
       for k in range(l):
        
            if slist[k] > slist[k + 1]:
                
                temp = slist[k]
                slist[k] = slist[k + 1]
                slist[k + 1] = temp
                
            l -= 1
            
    return slist

slist1 = [2,8,7,9]
print("Prior to bubblesort: ", slist1)
print("After bubblesort: ", bubblesort(slist1))
