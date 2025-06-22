from array import *
#1.Create an array and traverse
my_array = array('i',[1,2,3,4,5])
my_arr = [1,3,4,6,7]

for i in my_array:
    print(i)

#2.Access individual elements through indexes
print("Step 2:",my_array[2])

#3.Append any value to the array using append() method
my_array.append(8)
print("Step 3:",my_array)

#4.Insert value in an array using insert() method
my_array.insert(0,10)
print("Step 4:",my_array)

#5.Extend python array using extend() method
my_array_1 = [9,0,2]
my_array.extend(my_array_1)
print("Step 5:",my_array)

#6.Add items from list into array using fromlist() method
tempList = [20,21,22]
my_array.fromlist(tempList)
print("Step 6:",my_array)

#7.Remove any element from array using remove() method
my_array.remove(10)
print("step 7:",my_array)

#8.Remove last element from array using pop() method
my_array.pop()
print("Step 8:",my_array)

#9.Fetch any element through its index using index() method
print("Step 9:",my_array.index(21))

#10.Reverse a python array using reverse() method
my_array.reverse()
print("Step 10:",my_array)

#11.Get array buffer information through buffer_info() method
print("Step 11:",my_array.buffer_info())

#12.Check for number of occurences of an element using count()method
my_array_count = my_array.count(20) #counts the value 20 in the array
print("Step 12:", my_array_count)

#13.Convert array to string using toString() method
#temp_str = my_array.tostring()
#print(temp_str)

#14.Convert an array to python list with same elements using tolist() method
my_array.tolist()
print("Step 14:",my_array)
#15.Append a string to char array using fromstring() method
#16.Slice elements from an array
print("Step 16:",my_array[2:])


