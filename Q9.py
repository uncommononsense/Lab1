# 9. Write a function replatind(array,position,element) to replace an element into an array at the specified index (position).


arr=[1,4,2,3]

def replatind(a,p,e):
    if(p>len(a)):
        return -1
    
    k = [None]*(len(a))
    for i in range(p-1):
        k[i]=a[i]
    for i in range(p,len(a)):
        k[i]=a[i]
    k[p-1]=e 
    return k

print(replatind(arr,3,5))