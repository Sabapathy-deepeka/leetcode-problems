# List is contiguous in memory so that it can be accessed by indexes
# Linkedlist is spread out in memory but can be refered by the pointers that refer to next
# Every node in the linked list is a dictionary with value and pointer

"""
Big O notation for LinkedList operations:

Append -append at end- append an element to the LL at the end - O(1)
Pop - remove at end - after removing the last element, to point tail to the last element 
                      we need to traverse from head to find the tail - O(n)
Prepend- appending at beginning - O(1)
Pop First -removing at beginning - O(1)
Insert- appending at middle - starts from head to iterate through the middle- O(n)
Remove - removing at middle - O(n)
Lookup for an element by index/value - Need to iterate from head - O(n)

"""
class Node: # Creating a class for node creation to reuse for every node creation
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self,value): 
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append_linked_list(self,value):
        new_node = Node(value)
        if self.head is None: # checking the edge case if linkedlist is empty
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True
    
    def pop(self):
        if self.length == 0:
            return None
        #Creating two variables pre and temp to traverse through LL and pop
        temp = self.head
        pre = self.head
        while(temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0: #This is to check for edge case where there is one node, head and tail points to the same
            self.head = None
            self.tail = None
        return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0: #edge case to check one item
            self.tail = None    

    def print_linked_list(self):
        temp =  self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def get(self,index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
    
    def set_value(self, index, value):
        temp = self.get(index)
        if temp is not None:
            temp.value = value
            return True
        return False
    
    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append_linked_list(value)
        new_node = Node(value)
        temp = self.get(index - 1) #going to the index before where new value needs to ne inserted
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True
    
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        prev = self.get(index -1)
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        self.length -= 1
        return temp
    
    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after


#calls all methods
linked_list = LinkedList(1)

linked_list.append_linked_list(2)
linked_list.append_linked_list(3)
linked_list.append_linked_list(4)

print(linked_list.pop())

linked_list.prepend(0)
linked_list.prepend(10)

linked_list.pop_first()

linked_list.print_linked_list()

print("Get Item",linked_list.get(2))

linked_list.set_value(1,4)

linked_list.insert(2,5)

linked_list.remove(2)

linked_list.print_linked_list()