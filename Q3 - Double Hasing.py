"""
hp(key) = 1 + key%p
p<m
slot = (home + i*hp(key))%m
p = 11
m = 17
"""
class DoubleHashTable():
    def __init__(self,capacity,key):
        self.capacity = capacity
        self.values = capacity*[None]
        self.size = 0
        self.p = key
    
    def insert(self,value):
        assert self.capacity !=self.size, "HashTable is full!"
        m = self.capacity
        p = self.p
        home = value
        hp = 1 + value%p
        i = 0
        while(self.values[(home + i*hp)%m]!=None):
            i+=1
        self.values[(home + i*hp)%m] = value
        self.size+=1
    
    def printTable(self):
        n = self.capacity
        for i in range(n):
            print(self.values[i],end=" ")
        print()

    def contains(self,value):
        m = self.capacity
        p = self.p
        home = value
        hp = 1 + value%p
        i = 0
        c=0
        while(self.values[(home + i*hp)%m]!=value):
            if(c==self.size):
                return print("False")
            i+=1
            c+=1
        return print("True")
    
    def findPosition(self,value):
        m = self.capacity
        p = self.p
        home = value
        hp = 1 + value%p
        i = 0
        c=0
        while(self.values[(home + i*hp)%m]!=value):
            if(c==self.size):
                return print("Value does not exist in the table")
            i+=1
            c+=1
        return (home + i*hp)%m

    def numOfColl(self,value):
        m = self.capacity
        m = self.capacity
        p = self.p
        home = value
        hp = 1 + value%p
        i = 0
        c=0
        while(self.values[(home + i*hp)%m]!=value):
            if(c==self.size):
                return print("Value does not exist in the table")
            i+=1
            c+=1
        return i
        
    

l = DoubleHashTable(17,11)
listValues = [133,88,92,221,174]
n = len(listValues)
for i in range(n):
    l.insert(listValues[i])

l.printTable()

checkList = [100,133,174]
n1 = len(checkList)
for i in range(n1):
    l.contains(checkList[i])
        