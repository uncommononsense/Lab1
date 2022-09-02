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
# 8 a. Write a function linsatbeg(linked_list, element) that inserts an element at the beginning of the linked list.
def linsatbeg(L1,e):

    new = ListNode(e)
    new.next = Linklist.head
    Linklist.head = new

print(linsatbeg(Linklist,0))
head = Linklist.head

while(head != None):
    print(head.data, end=" ")
    head = head.next
    

# 8 b. Write the function delatend(linked_list) that deletes the last element of the linked list.
def delatend(_list):
    tail = Linklist.tail
    head = Linklist.head
    while(head != tail):
        print(head.data,end=" ")
        head = head.next
print("")
print(delatend(Linklist))