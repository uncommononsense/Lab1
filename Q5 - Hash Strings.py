
class StringHashTable():
    def __init__(self,capacity):
        self.capacity = capacity
        self.size=0
        self.values = [None]*capacity

    def insert(self,str):
        assert self.size!=self.capacity, "HashTable is full!"
        a = 2
        ans = 0
        n = len(str)
        c = 1
        m = self.capacity
        for i in str:
            ans+= ord(i)*pow(a,n-c)
            c+=1
        pos = ans%m
        self.values[pos] = str
        self.size+=1
        print(f"The string is {str}. Value of Polynomial {ans}, it will be inserted at {pos}")

    def contains(self,str):
        a = 2
        ans = 0
        n = len(str)
        c = 1
        m = self.capacity
        for i in str:
            ans+= ord(i)*pow(a,n-c)
            c+=1
        pos = ans%m
        return self.values[pos]==str
    
    def printTable(self):
        n = self.capacity
        for i in range(n):
            print(self.values[i],end=" ")

l = StringHashTable(17)
li = ["fist","sift","shift","fast","faster","shaft"]
for i in li:
    l.insert(i)

l.printTable()
print()
print()
l1 = StringHashTable(37)
li = ["fist","sift","shift","fast","faster","shaft"]
for i in li:
    l1.insert(i)

l1.printTable()

