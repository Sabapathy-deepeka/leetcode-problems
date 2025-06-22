"""
Used so that we dont need to create 100 variables to store 100 values

Array Types: One dimensional/ Multi dimesional

One dimensional :Simplest linear array a[i]-> i between 0 and n
Two dimensional: a[row_index][column_index]->to access a element
Three dimensional: a[depth_index][row_index][column_index]

Array Memory: Array elements are represented as a single row continuously in memory not shattered
(even Two/three dimesional arrays are represented as single row in memory)
"""

import array
import numpy as np
from array import *

my_array = array('i') #Empty array
print(my_array)
my_array_i = array('i',[1,2,3,4])
my_array_i.insert(4,6)
print(my_array_i)

#Time and Space complexity to create an array with elements is O(N)

np_array = np.array([1,2,6,8],dtype=int)
print(np_array)


arr1 = array('i',[1,2,3,4,5,6])
arr2 = array('d',[1.3,1.4,1.6])

#Remove a element from array
#If last element is removed time complexity is O(1), else for middle elements it is O(n)
#Space complexity is always O(1) as we dont need extra space
arr2.remove(1.4) 
print(arr2)

#array traversal
def traversalArray(array): 
    for i in array: #O(n)
        print(i)  #O(1) So overall time complexity O(n)


#Another way to access an element
def access_element(array,index):
    if index >= len(array):
        print("No element for the index")
    else:
        print(array[index]) #In this way time complexity is O(1) for all lines so overall O(1)

def linear_search(array,target):
    for i in range(len(array)):
        if array[i] == target:
            print("Element found", i)
    return -1



print('Array Traversal:')
traversalArray(arr1)
print('Access an Element:')
access_element(arr1, 2)
print('Search an Element:')
linear_search(arr1,4)
