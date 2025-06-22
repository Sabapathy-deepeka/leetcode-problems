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
    
    def partition_list(self,x):
        current = self.head 
        left = Node(0)
        right = Node(0)
        left_tail = left
        right_tail = right
        if current is None:
            return None
        while current:
            if current.value < x:
                left_tail.next = current
                left_tail = left_tail.next
            else:
                right_tail.next = current
                right_tail = right_tail.next
            current = current.next

        left_tail.next = right.next #we do right.next as right is a dummy node, right.next has the actual node
        right_tail.next = None
        return left.next #as left is just a dummy node


linked_list = LinkedList(3)
linked_list.append(8)
linked_list.append(5)
linked_list.append(10)
linked_list.append(2)
linked_list.append(1)
print(linked_list.partition_list(5))