# 3. Write a function delatind(array,position) to delete an element in an array at the specified index(position).

arr=[1,4,2,3]

def delatind(a,p):
    
    k = [None]*(len(a)-1)
    for i in range(p-1):
        k[i]=a[i]
    for i in range(p,len(a)):
        k[i-1]=a[i]
    return k

print(delatind(arr,2))