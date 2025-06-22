'''
Binary Search Tree - Every Node points to 0 or two nodes

Full - Every node points to 0 or 2 nodes
Perfect - Any node in the tree is filled across all the nodes
Complete - Filling the tree from left to right with no gaps for a node
Parent - Has child nodes(child nodes are also called siblings), it cannot have two parents
On BST - Number greater than parent , will go on right 
         Number less than parent, will go on left

Time Complexity - O(log N)
We can get to a specific node by 2 power of (level) - 1 --> 2(2) - 1  also gives number of elements
In case BST has only right side of elements and tree does not fork - it is almost a linked list so
to traverse through elements it is O(N)


Big O Comparison BST and LL

BST 
Insert - (O log N), if tree does not fork worst case O(N)
Lookup - (O log N)
Remove - (O log N)

LL
LL is a good data structure if huge burst data need to be captured/inserted at high speed but we dont often need to lookup for that data
Insert -  Very quick to insert at the end - O(1)
Lookup & Remove by value - O(N)
'''

class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class binarySearchTree:
    def __init__(self):
        self.root = None

    #To insert- step 1: create a new node
    #           step 2: if new node < root --> left or new node > root --> right
    #           step 3: if None insert new_node else move to next level
    #           step 2 and 3 keeps repeating, so should be inside the loop- While loop
    #           Edge Case: New Node cannot be equal to any node in tree, if so return False
    def insert(self,value):
        new_node = Node(value)
        if self.root == None:
            self.root = new_node
            return True
        temp = self.root
        while True:
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right
    

    def contains(self,value):
        if self.root == None:
            return False
        temp = self.root
        while temp is not None:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            elif value == temp.value:
                return True
        return False
    


    
my_tree = binarySearchTree()
my_tree.insert(2)
my_tree.insert(1)
my_tree.insert(3)

print(f"Root:{my_tree.root.value} Left:{my_tree.root.left.value} Right:{my_tree.root.right.value}")
print(my_tree.contains(3))
print(my_tree.contains(5))

   
