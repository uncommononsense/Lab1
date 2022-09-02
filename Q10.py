# 10. Write a function replatind(linked_list,position,element) to replace an element in the linked list at the specified position.
class ListNode:
    def __init__(self, data):
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


def replatind(L1, p, e):
    New = ListNode(e)
    head1 = L1.head
    l = 0
    n = 0

    while (l != p-1):
        l = l+1
    while (l != n):
        head1 = head1.next
        if(head1 == None):
            return -1
            break
        n = n+1

    head1.data = New.data


print(replatind(Linklist, 6, 7))
head = Linklist.head
while (head != None):
    print(head.data, end=" ")
    head = head.next