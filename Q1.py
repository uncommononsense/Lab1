# 1. Write function srch(array,element) that searchs the array fot the element and returns the index (position) in the array if the elemtn is found, and -1 otherwise.

array1 = [1,4,3,2]
def srch(a,e):
    for i in range(len(a)):
        if(e==a[i]):
            return i+1
    return -1

print(srch(array1,2))
print(srch(array1,6))