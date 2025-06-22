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
    
    def reverse_between(self, s_index, e_index):
        current_start = self.head
        current_end = self.head
        if self.head is None:
            return None
        for _ in range(s_index):
            current_start = current_start.next
        for _ in range(e_index):
            current_end = current_end.next
        return current_end
        
        
        

        

    
linked_list = LinkedList(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)

print(linked_list.reverse_between(2,4).value)
    