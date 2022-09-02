# 5. Write a function insatbeg(array,element) that inserts an element at the beginning of the array.

arr=[1,4,2,3]

def insatbeg(a,e):
    k=[None]*(len(a)+1)
    k[0]=e
    for i in range(len(k)-1):
        k[i+1]=a[i]
    return k
print(insatbeg(arr,55))