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

# 6. Write a function Isrch(linked_list,element) that searches a linked list for the element and return the index(position) in the linked list if the element is found, and -1 otherwise.
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


# 7. Write a function linsatend(linked_list, element) that inserts an element at the end of a linked list.
def linsatend(L1,e):
    newNode = ListNode(e)
    L1.tail.next = newNode
    L1.tail = L1.tail.next

    tmp = Linklist.head
    while tmp != None:
        print(tmp.data, end=" ")
        tmp = tmp.next
    
print((linsatend(Linklist,5)))


# 8 a. Write a function linsatbeg(linked_list, element) that inserts an element at the beginning of the linked list.
def linsatbeg(L1,e):

    new = ListNode(e)
    new.next = L1.head
    L1.head = new

print(linsatbeg(Linklist,0))
head = Linklist.head

while(head != None):
    print(head.data, end=" ")
    head = head.next
    

# 8 b. Write the function delatend(linked_list) that deletes the last element of the linked list.
def delatend(_list):
    tail = _list.tail
    head = _list.head
    while(head != tail):
        print(head.data,end=" ")
        head = head.next
print("")
print(delatend(Linklist))


# 10. Write a function replatind(linked_list,position,element) to replace an element in the linked list at the specified position.
def replatind(L1,p,e):
    New = ListNode(e)
    head1 = L1.head
    l=0
    n=0
    m=0

    while (l != p-1):
        l = l+1
    
    while (l != n):
        head1 = head1.next
        if(head1 == None):
            return -1
            break
        n=n+1
    
    head1.data = New.data

print(replatind(Linklist,3,7))
head = Linklist.head
while(head != None):
    print(head.data,end=" ")
    head = head.next