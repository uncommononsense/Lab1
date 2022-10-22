
class HashTable():
    def __init__(self,capacity):
        self.capacity = capacity
        self.values = capacity*[None]
        self.size=0
    
    def insert(self,value):
        assert self.size!=self.capacity,"HashTable is full!"
        m = self.capacity
        home = value
        i = 0
        while(self.values[(home+i*i)%m]!=None):
            i+=1
        self.values[(home+i*i)%m] = value
        self.size+=1
        
    def printTable(self):
        n = self.capacity
        for i in range(n):
            print(self.values[i],end=" ")
        print()

    def contains(self,value):
        c=0
        m = self.capacity
        home = value
        i = 0
        while(self.values[(home+i*i)%m]!=value):
            if(c==self.size):
                return print ("False")
            i+=1
            c+=1

        return print("True")

    def FindPosition(self,value):
        c=0
        m = self.capacity
        home = value
        i = 0
        while(self.values[(home+i*i)%m]!=value):
            if(c==self.size):
                return print ("False")
            i+=1
            c+=1

        return (home+i*i)%m

    def numOfColl(self,value):
        c=0
        m = self.capacity
        home = value
        i = 0
        while(self.values[(home+i*i)%m]!=value):
            if(c==self.size):
                return print ("value does not exist in the table")
            i+=1
            c+=1
        return i


l = HashTable(17)
# listValues = [133,88,92,221,174]
# n = len(listValues)
# for i in range(n):
#     l.insert(listValues[i])

# l.printTable()

# checkList = [100,133,174]
# n1 = len(checkList)
# for i in range(n1):
#     l.contains(checkList[i])

# l1 = HashTable(37)
# for i in range(n):
#     l1.insert(listValues[i])

# l1.printTable()

# for i in range(n1):
#     l1.contains(checkList[i])


collList = [19, 24, 36, 34, 45, 51, 64, 81, 82, 75, 119, 113, 125, 130, 165, 183, 200] #Sequence which is not random(I decided some values)
collList2 = [36, 61, 71, 78, 92, 106, 111, 114, 127, 141, 142, 143, 145, 155, 167, 175, 194] #Sequence generated using random generator
l1 = HashTable(17)
for i in collList:
    l.insert(i)

for i in collList:
    n = l.numOfColl(i)
    print(f"{i} had this many collisons:{n}")
print()
print()

# for i in collList2:
#     l1.insert(i)
# for i in collList2:
#     n = l1.numOfColl(i)
#     print(f"{i} had this many collisons:{n}")

