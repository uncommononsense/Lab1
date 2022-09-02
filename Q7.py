# 7. Write a function linsatend(linked_list, element) that inserts an element at the end of a linked list.
class ListNode:
    def __init__(self,data):
        self.data = data
        self.next = None
class linklist():
    def __init__(self):
        self.head = None
        self.tail = None
Linklist = linklist()
a = ListNode(1)
Linklist.head = a
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
a.next = b
b.next = c
c.next = d
Linklist.tail = d
d.next = None

def linsatend(L1,e):
    newNode = ListNode(e)
    L1.tail.next = newNode
    L1.tail = L1.tail.next

    tmp = Linklist.head
    while tmp != None:
        print(tmp.data, end=" ")
        tmp = tmp.next
    
print((linsatend(Linklist,5)))