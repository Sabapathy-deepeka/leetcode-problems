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
    
def kth_node_from_end(linked_list, k):
    slow = fast= linked_list.head
    for _ in range(k):
        if fast is None:
            return None
        fast = fast.next
    while fast is not None:
        slow = slow.next
        fast = fast.next
    return slow


linked_list = LinkedList(1)

linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)
linked_list.append(6)
print(kth_node_from_end(linked_list,2).value)