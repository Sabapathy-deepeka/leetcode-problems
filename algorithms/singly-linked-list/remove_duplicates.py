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
    
    def remove_duplicates(self):
        current = self.head
        last_unique = None
        values  = set()
        while current:
            if current.value in values:
                last_unique.next = current.next
                self.length -= 1
            else:
                values.add(current.value)
                last_unique = current
            current = current.next
        return values


linked_list = LinkedList(1)

linked_list.append(2)
linked_list.append(1)
linked_list.append(4)
linked_list.append(5)
linked_list.append(4)
print(linked_list.remove_duplicates())