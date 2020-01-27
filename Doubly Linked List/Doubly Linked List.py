#!/usr/bin/env python
# coding: utf-8

# In[4]:


class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None
    
class Double:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def insertAtFirst(self,val):
        if self.head == None and self.tail == None:
            x = Node(val)
            self.head = x
            self.tail = x
        else:
            x = Node(val)
            temp = self.head
            self.head = x
            x.next = temp
            temp.prev = x
            
    def insertAtLast(self,val):
        if self.head == None and self.tail == None:
            x = Node(val)
            self.head = x
            self.tail = x
        else:
            x = Node(val)
            temp = self.tail
            self.tail = x
            temp.next = x
            x.prev = temp
            
    def insertAfter(self,addr,val):
        if self.head == None and self.tail == None:
            print("List is empty")
        else:
            temp = self.head
            while temp:
                if temp.value == addr:
                    x = Node(val)
                    temp2 = temp.next
                    temp.next = x
                    x.prev = temp
                    temp2.prev = x
                    x.next = temp2
                    return
                temp = temp.next
            print("Value not found")
            
    def Sum(self):
        temp = 0
        x = self.head
        while x:
            temp += x.value
            x = x.next
        return temp
    
    def DeleteFirst(self):
        if self.head == None and self.tail == None:
            print("list is empty")
        elif self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            x = self.head
            y = x.next
            self.head = y
            y.prev = None
            
    def DeleteLast(self):
        if self.head == None and self.tail == None:
            print("list is empty")
        elif self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            x = self.tail
            y = x.prev
            self.tail = y
            self.tail.next = None
            
    def DeleteVal(self,val):
        if self.head == None and self.tail == None:
            print("List is Empty")
        elif self.head == self.tail and self.head.value == val:
            self.head = None
            self.tail = None
        else:
            if self.tail.value == val:
                self.DeleteLast()
                return
            elif self.head.value == val:
                self.DeleteFirst()
                return
            else:
                temp = self.head
                while temp:
                    if temp.value == val:
                        temp.prev.next = temp.next
                        temp.next.prev = temp.prev
                        return
                    temp = temp.next
                print("Value not found")
            
    def DeleteAllVal(self,val):
        if self.head == None and self.tail == None:
            print("List is Empty")
        elif self.head == self.tail and self.head.value == val:
            self.head = None
            self.tail = None
        else:
            if self.tail.value == val:
                self.DeleteLast()
                self.DeleteAllVal(val)
                return
            elif self.head.value == val:
                self.DeleteFirst()
                self.DeleteAllVal(val)
                return
            else:
                temp = self.head
                while temp:
                    if temp.value == val:
                        temp.prev.next = temp.next
                        temp.next.prev = temp.prev
                        self.DeleteAllVal(val)
                        return
                    temp = temp.next
    
    def Print(self):
        if self.head == None and self.tail == None:
            print("[]")
        else:
            x = self.head
            print("[",end="")
            while x:
                print(x.value,end="")
                if x.next != None:
                    print(",",end=" ")
                else:
                    print("]")
                x = x.next
    
    def PrintRev(self):
        if self.head == None and self.tail == None:
            print("[]")
        else:
            x = self.tail
            print("[",end="")
            while x:
                print(x.value,end="")
                if x.prev != None:
                    print(",",end=" ")
                else:
                    print("]")
                x = x.prev
                
    def Length(self):
        length = 0
        x = self.head
        while x:
            length += 1
            x = x.next
        return length

            
d1 = Double()
d1.insertAtFirst(5)
d1.insertAtFirst(6)
d1.insertAtFirst(7)
d1.insertAtLast(10)
d1.insertAtLast(99)
d1.insertAfter(10,8)
d1.insertAfter(10,7)
d1.insertAtLast(7)
d1.insertAfter(5,7)
#d1.DeleteLast()
d1.DeleteAllVal(7)
d1.insertAfter(8,6)
d1.DeleteVal(6)
#d1.DeleteFirst()
d1.Print()
print("Sum:",d1.Sum())
d1.PrintRev()
print("Length:",d1.Length())


# In[ ]:





# In[ ]:





# In[ ]:




