"""
Heaps are always 'COMPLETE' trees, where the tree is filled from left to right
In MAX heaps- the parent node is greater or equal to child
In MIN heaps- the parent node is lesser or equal to child

Heap Insertion - We first insert to the available spot, and compare it with parent and keep swapping

If we are inserting into index 0 
TO get through the child index  
Left =  2 * parent index + 1
Right =  2 * parent index + 2 

To get to a parent node 
Left child = index-1 // 2
Right child = index-1 // 2 - just takes the absolute
"""
class MaxHeap:
    def __init__(self):
        self.heap = []
    
    def left_child(self, index):
        return 2 * index + 1
    
    def right_child(self, index):
        return 2 * index + 2
    
    def parent(self, index):
        return(index - 1) // 2
    
    def swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def insert(self, value):
        self.heap.append(value)
        current = len(self.heap) - 1
        while current > 0 and self.heap[current] > self.heap[self.parent(current)]:
            self.swap(current,self.parent(current))
            current = self.parent(current)
    
    def remove(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        max_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.sink_down(0)

        return max_value


my_heap = MaxHeap()
my_heap.insert(99)
my_heap.insert(72)
my_heap.insert(61)
my_heap.insert(58)
print(my_heap.heap)
my_heap.insert(100)
print(my_heap.heap)        