# Stacks - LIFO - More similar implementation using linked list 
# Here we refer HEAD and TAIL as TOP and BOTTOM(not required), because we pop/push from top
# We refer length as height

class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class stacks:
    def __init__(self,value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    def print_stack(self):
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next
    
    def push_stack(self,value):
        new_node = Node(value)
        if self.top == None:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1
    
    def pop_stack(self):
        temp = self.top
        if self.height == 0:
            return None
        else:
            self.top = self.top.next
            temp.next = None #To remove the node from stack
        self.height -= 1
        return temp

my_stack = stacks(4)
my_stack.push_stack(3)
my_stack.push_stack(2)
my_stack.pop_stack()
my_stack.print_stack()

            
    
