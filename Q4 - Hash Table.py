class bitsHashTable():
    def __init__(self,capacity):
        self.capacity = capacity
        self.values = [0]*capacity
        self.size = 0
    
    def insert(self,value):
        assert self.size!=self.capacity, "Hashtable is full!"
        m = self.capacity
        self.values[value%m] = 1
        self.size+=1
    
    def printTable(self):
        n = self.capacity
        for i in range(n):
            print(self.values[i],end = ' ')
        print()

    def contains(self,value):
        c = 0
        m = self.capacity
        home = value
        return self.values[home%m]==1
        


checkList = [133,88,92,221,174]
l = bitsHashTable(17)
l1 = bitsHashTable(37)
for i in checkList:
    l.insert(i)
    l1.insert(i)

li = [100,133,174]
for i in li:
    if(l.contains(i) and l1.contains(i)):
        print("True")
    else:
        print("False")


    




    