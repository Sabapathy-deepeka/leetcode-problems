"""
Given the head of a singly linked list, return the middle node of the linked list.

Example 1:
Input: LL = [1,2,3,4,5]
Output: 3
Explanation: The middle node of the list is node 3.

Example 2:
Input: LL = [1,2,3,4,5,6]
Output: 4
Explanation: Since the list has two middle nodes with values 3 and 4, we return the first element of second set.
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

    def append(self,value):
        new_node = Node(value)
        if self.head is None: # checking the edge case if linkedlist is empty
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        return True
    
    def find_middle_node(self):
        slow = self.head
        fast = self.head
        while(fast is not None and fast.next is not None):
            slow = slow.next
            fast = fast.next.next
        return slow


linked_list = LinkedList(1)

linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)
linked_list.append(6)

print(linked_list.find_middle_node().value)

    