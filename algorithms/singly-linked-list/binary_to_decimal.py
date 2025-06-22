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

    def append(self,value):
        new_node = Node(value)
        if self.head is None: # checking the edge case if linkedlist is empty
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1
        return True
    
    def binary_to_decimal(self):
        current = self.head
        decimal = 0
        while current:
           decimal = decimal * 2 + current.value
           current = current.next
        return decimal
                     

linked_list = LinkedList(1)

linked_list.append(0)
linked_list.append(1)
linked_list.append(1)
print(linked_list.binary_to_decimal())
