"""
Data Structures -  Way of organizing data
Algorithm - Steps to accomplish a task 
Good Algorithm - Correctness and Efficiency

Python has two types of data structures: 

Primitive(Integer, Float, String, Boolean) - Used for basic operations
Non Primitive - has two types linear and non linear

Linear: Data arranged in sequential order (List, Tuple, Array, LinkedList, Stack, Queue)
        List and tuple are build in data structures, others are user defined

Non-Linear: Not arranged in sequential order, used to represent hierarchial representation between elements
            (Set, Dictionary, Tree, Graph)
            Set and Dictionary are built in data structures
            Others are user defined-Needs a external library/needs to be defined by user

Types of Algorithms:
Sorting
Search
Graph

Big O : Metric used to describe the efficiency of the algorithm
Time Complexity : A way of showing how the runtime of a function increases 
                   as the size of input increases
Space Complexity : Amount of memory the code occupies


Complexities:
O(1): constant - Ex: A simple add numbers function (Any assignment statement/if statement that executes once regardless of size of the problem)
O(N): Linear - Ex: Loop through numbers from 1 to N
O(logN): Logarithmic - Ex: Find an element in sorted array (Controlling parameter is divided by two at each step)
O(N (square)2): Quadratic - Ex: Nested Loops
O(2 power N): Exponential - Ex: Double recursion in fibonacci

Example Code
O(1):
def multiple(n):
        n*n

O(N):
def print_items(n):
for i in range(n):
        print(i)
for j in range(n):
        print(j)

Even in case there are multiple loops it will be n+n = 2n but we drop constants as 
it does not make a big difference and depends on computer speed/memory

O(N sqaure):
Nested loop
def print_items(n):
for i in range(n): ---O(n)
 for j in range(n): ----O(n) so n*n = nsquare
        print(i,j)

O(logN)- Example: Divide and conquer

---------Tricky Interview Question---------------
def print_items(a,b):
for i in range(a): --O(a)
        print(i)
for j in range(b): --O(b)
        print(j)

Finally : O(a)+O(b)=O(a+b)

def print_items(a,b):
for i in range(a): --O(a)
        for j in range(b): --O(b)
          print(i,j)

Nested Loop and so final time complexity : O(a*b)


"""


