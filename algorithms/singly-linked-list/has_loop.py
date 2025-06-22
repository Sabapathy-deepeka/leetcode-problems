# Find if there is a loop in the linked list


class Node: # Creating a class for node creation to reuse for every node creation
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self,value): 
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node

    def append(self,value):
        new_node = Node(value)
        if self.head is None: # checking the edge case if linkedlist is empty
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        return True

    def has_loop(self):
        slow = self.head
        fast = self.head
        while(fast is not None and fast.next is not None):
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
        


linked_list = LinkedList(1)

linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)
linked_list.append(6)
linked_list.tail.next = linked_list.head
print(linked_list.has_loop())
