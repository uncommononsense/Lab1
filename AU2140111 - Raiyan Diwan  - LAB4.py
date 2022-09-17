#!/usr/bin/env python
# coding: utf-8

# In[13]:


class Stack:
    def __init__(self):
        self.tail = None
        self.head = None
    
    def push(self, item):
        new_item = Node(item)
        if self.tail == None:
            self.head = new_item
            self.tail = new_item
        else:
            self.tail.next = new_item
            self.tail = new_item
            
    def peek(self):
        assert self.is_empty() != True, "The stack is empty"
        return(self.tail.val)
            
    def is_empty(self):
        if self.tail == None:
            return True
        else:
            return False
        
    def __len__(self):
        curr = self.head
        l = 0
        while curr != None:
            l += 1
            curr = curr.next
        return l
    
    def pop(self):
        assert self.is_empty() != True, "The stack is empty"
        if self.head.next == None:
            popped = self.head.val
            self.tail = None
            self.head = None
            return popped
        prev = self.head
        while prev.next.next != None:
            prev = prev.next
        popped = prev.next.val
        prev.next = None
        self.tail = prev
        return popped
            
    def print_stack(self):
        curr = self.head
        while curr != None:
            print(curr.val)
            curr = curr.next
        
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


# In[14]:


stack = Stack()
stack.push(2)
stack.push(3)
stack.push(1)
stack.push(5)
print(stack.peek())


# In[15]:


def postfix(string):
    stck = Stack()
    inps = string.split()
    i = 0
    while i < len(inps):
        if inps[i] == "+":
            t1 = int(stck.pop())
            t2 = int(stck.pop())
            stck.push(t1 + t2)
        elif inps[i] == "-":
            t1 = int(stck.pop())
            t2 = int(stck.pop())
            stck.push(t2 - t1)
        elif inps[i] == "*":
            t1 = int(stck.pop())
            t2 = int(stck.pop())
            stck.push(t1 * t2)
        elif inps[i] == "/":
            t1 = int(stck.pop())
            t2 = int(stck.pop())
            stck.push(t2 / t1)
        else: 
            stck.push(inps[i])
        i += 1
    print(stck.peek())
postfix("5 5 + 5 / 2 * 1 -")


# In[47]:


def balance(string):
    stck = Stack()
    inps = string.split()
    i = 0
    while i < len(inps):
        if inps[i] == "//":
            if stck.__len__() != 0:
                return False
            else:
                return True
        if inps[i] == "(":
            stck.push(inps[i])
        if inps[i] == "[":
            stck.push(inps[i])
        if inps[i] == "{":
            stck.push(inps[i])
        if inps[i] == ")":
            if stck.__len__() != 0:
                stck.pop()
            else:
                return False
        if inps[i] == "]":
            if stck.__len__() != 0:
                stck.pop()
            else:
                return False
        if inps[i] == "}":
            if stck.__len__() != 0:
                stck.pop()
            else:
                return False
        i += 1
    if stck.__len__() != 0:
        return False
    else:
        return True

balance("void main ( num )  print { ( Hello World ) } [ ]")


# In[2]:


class PriorityQueue3:
    def __init__(self):
        self.q1 = None
        self.q2 = None
        self.q3 = None

    def enqueue(self, value, pr):
        new = Node(value)
        if pr == 1:
            if self.q1 == None:
                self.q1 = new
            else:
                curr = self.q1
                while curr.next != None:
                    curr = curr.next
                curr.next = new
        elif pr == 2:
            if self.q2 == None:
                self.q2 = new
            else:
                curr = self.q2
                while curr.next != None:
                    curr = curr.next
                curr.next = new
        elif pr == 3:
            if self.q3 == None:
                self.q3 = new
            else:
                curr = self.q3
                while curr.next != None:
                    curr = curr.next
                curr.next = new
        else:
            print("Please enter a valid priority of 1-3")

    def dequeue(self):
        if self.q1 == None and self.q2 == None and self.q3 == None:
            print("The queue is already empty!!")
        else:
            if self.q1 == None:
                if self.q2 == None:
                    popped = self.q3
                    self.q3 = self.q3.next
                    return popped.val
                else:
                    popped = self.q2
                    self.q2 = self.q2.next
                    return popped.val
            else:
                popped = self.q1
                self.q1 = self.q1.next
                return popped.val                

    def __len__(self):
        i = 0
        curr = self.q1
        while curr != None:
            i += 1
            curr = curr.next
        curr = self.q2
        while curr != None:
            i += 1
            curr = curr.next
        curr = self.q3
        while curr != None:
            i += 1
            curr = curr.next
        return i        

    def isNull(self):
        return self.q1 == None and self.q2 == None and self.q3 == None

    def peek(self):
        if self.q1 == None:
            if self.q2 == None:
                return self.q3.val
            else:
                return self.q2.val
        else:
            return self.q1.val

    def print_queue(self):
        curr = self.q1
        print("Priority-1")
        while curr != None:
            print(curr.val)
            curr = curr.next
        curr = self.q2
        print("Priority-2")
        while curr != None:
            print(curr.val)
            curr = curr.next
        curr = self.q3
        print("Priority-3")
        while curr != None:
            print(curr.val)
            curr = curr.next
    
        
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


# In[3]:


p1 = PriorityQueue3()
p1.enqueue(5,1)
p1.enqueue(2,3)
p1.enqueue(6,2)
p1.enqueue(7,1)
p1.dequeue()
p1.peek()
p1.dequeue()
p1.peek()
p1.__len__()


# In[4]:


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def enqueue(self, value):
        new = Node(value)
        if self.head == None and self.tail == None:
            self.head = new
            self.tail = new
        else:
            self.tail.next = new
            self.tail = new
        self.length += 1

    def dequeue(self):
        assert self.head != None, "The queue is already empty"
        dequeued_val = self.head
        self.head = self.head.next
        self.length -= 1
        return dequeued_val.val
    
    def __len__(self):
        return self.length

    def isNull(self):
        return self.length == 0

    def peek(self):
        assert not self.isNull(), "The queue is empty"
        return self.head.val

    def print_queue(self):
        curr = self.head
        while curr != None:
            print(curr.val)
            curr = curr.next
    
        
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


# In[5]:


q1 = Queue()
q1.enqueue(1)
q1.enqueue(2)
q1.enqueue(3)
q1.dequeue()
q1.__len__()


# In[ ]:




