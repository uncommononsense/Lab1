from re import M


class _2DHasing():
    def __init__(self,capacity):
        self.capacity = capacity
        self.size = 0
        self.values = [[None]*capacity for i in range(capacity)]
    
    def insert(self,value):
        m = self.capacity
        pos = value%m
        n = len(self.values[pos])
        assert n!=self.capacity, "Row is full!"
        self.values[pos][n-1] = value
        print(f'{value} got append to row {pos} at position {n-1}')

    def contains(self,value):
        m = self.capacity
        pos = value%m
        return value in self.values[pos]
    
    def printHashTable(self):
        m = self.capacity
        for i in range(m):
            for j in range(m):
                print(self.values[m][m],end = " ")
            print()
    
l = _2DHasing(9)

c = 1
for i in range(9):
    for j in range(9):
        l.insert(c)
        c+=1

l.printHashTable()




    