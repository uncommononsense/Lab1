# 4. Write a function insatend(array,element) that inserts an element at the end of an array.

arr=[1,4,2,3]

def insatend(a,e):

    k = [None]*(len(a)+1)
    for i in range(len(a)):
        k[i]=a[i]
    
    k[len(a)]=e 
    return k

print(insatend(arr,6))