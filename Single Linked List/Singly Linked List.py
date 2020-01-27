#!/usr/bin/env python
# coding: utf-8

# In[4]:


class node:
    def __init__(self,value):
        self.value = value
        self.next = None

class linkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insertAtFirst(self,val):
        x = node(val)
        if self.head == None and self.tail == None:
            self.head = x
            self.tail = x
        else:
            x.next = self.head
            self.head = x
            
    def insertAtLast(self,val):
        x = node(val)
        temp = self.tail
        if self.tail == None and self.head == None:
            self.tail = x
            self.head = x
        else:
            temp.next = x
            self.tail = x
            
    def insertAfter(self,addr,val):
        x = node(val)
        temp = self.head
        while temp:
            if addr == temp.value:
                if temp.next == None:
                    self.insertAtLast(val)
                else:
                    x.next = temp.next
                    temp.next = x
                break
            temp = temp.next
            
    def deleteAtFirst(self):
        if self.head == None and self.tail == None:
            print("List is Empty")
        elif self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            x = self.head
            self.head = x.next
        
    def deleteAtLast(self):
        if self.head == None and self.tail == None:
            print("List is Empty")
        elif self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            x = self.head
            y = x.next
            while y.next:
                x = x.next
                y = y.next
            x.next = None
            self.tail = x
    
    def deleteVal(self,val):
        if self.head == None and self.tail == None:
            print("List is Empty")
        elif self.head == self.tail and self.head.value == val:
            self.head = None
            self.tail = None
        else:
            x = self.head
            y = x.next
            while y:
                if y.value == val:
                    x.next = y.next
                    break
                x = x.next
                y = y.next
            if not y:
                print("Value not found")
               
    def printList(self):
        print("[",end="")
        if self.head == None and self.tail == None:
            print("List is Empty")
        else:
            x = self.head
            while x:
                print(x.value,end="")
                if x.next != None:
                    print(",",end=" ")
                x = x.next
        print("]")
        
    def printReverse(self):
        x = self.__listR(self.head)
            
    def __listR(self,temp):
        while temp:
            self.__listR(temp.next)
            print(temp.value,end=" ")
            return temp
            
l1 = linkedList()
l1.insertAtFirst(5)
l1.insertAtLast(7)
l1.insertAtFirst(9)
l1.insertAtFirst(6)
l1.insertAfter(6,8)
l1.insertAtFirst(2)
l1.deleteAtFirst()
l1.deleteAtLast()
l1.deleteVal(9)
l1.insertAtFirst(2)
l1.insertAtLast(9)
l1.insertAfter(5,7)
l1.insertAfter(9,10)
l1.deleteVal(10)
l1.deleteAtFirst()
l1.deleteAtLast()
print("List: ",end="")
l1.printList()
print("List is reverse: ",end="")
l1.printReverse()


# In[ ]:




