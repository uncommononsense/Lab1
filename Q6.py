# 6. Write a function Isrch(linked_list,element) that searches a linked list for the element and return the index(position) in the linked list if the element is found, and -1 otherwise.
class ListNode:
    def __init__(self,data):
        self.data = data
        self.next = None
class linklist():
    def _init_(self):
        self.head = None
Linklist = linklist()
a = ListNode(1)
Linklist.head = a
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
a.next = b
b.next = c
c.next = d
d.next = None

def Isrch(L1,e):
    head = L1.head
    tmp = head
    i = 0
    flag = False

    while(tmp != None):
        i += 1
        if(tmp.data==e):
            print(i)
            flag = True 
            break
        tmp = tmp.next
    if(flag == False):
        return -1

print(Isrch(Linklist,3))