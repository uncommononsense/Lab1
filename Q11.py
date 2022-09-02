class DLListNode():
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class dlinklist():
    def __init__(self):
        self.head = None
        self.tail = None
DLinklist = dlinklist()
a = DLListNode(1)
dlinklist.head = a
b = DLListNode(2)
c = DLListNode(3)
d = DLListNode(4)


a.next = b
b.prev = a
b.next = c
c.prev = b
c.next = d
d.prev = c
dlinklist.tail = d
d.next = None

head = a
tail = d

def dubbly_append(dl1,e):
    new = DLListNode(e)

    head = dlinklist.head
    tail = dlinklist.tail

    tail.next = new
    new.prev = tail
    while(head != None):
        print(head.data,end=" ")
        head = head.next

print(dubbly_append(DLinklist,5))