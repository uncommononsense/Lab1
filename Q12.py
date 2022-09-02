# 12. Write a function dubbly_remove(dlinked_list, element) to remove an element from the doubly linked list.
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

def dubbly_remove(dl2,e):
    tail1 = dlinklist.tail
    head1 = dlinklist.head
    l=0
    n=0
    p=1
    while (head1.data != e):
        p = p+1
        head1 = head1.next
        if(head1 == None):
            return -1
            break
    head1 = dlinklist.head

    while(l != p-1):
        l = l+1

    while(l != n):
        head1 = head1.next
        n = n+1
    head1.data = 0

print(dubbly_remove(DLinklist,5))

head = dlinklist.head
while(head != None):
    if(head.data != 0):
        print(head.data,end=" ")
        head = head.next
    else:
        head = head.next