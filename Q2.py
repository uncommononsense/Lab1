# 2. Write a function insatind(array,position,element) to insert an element into an array at the specified index(position).

arr=[1,4,2,3]

def insatind(a,p,e):
    
    k = [None]*(len(a)+1)
    for i in range(p-1):
        k[i]=a[i]
    for i in range(p,len(a)+1):
        k[i]=a[i-1]
    k[p-1]=e 
    return k

print(insatind(arr,3,5))