"""
Hash table is a dictionary with - key, value pair
Hash has a mathematical function that runs, to determine the index, converts to list and stores at the index.
Hash math function can look at the key and determine the index 

Hash Collision:
We can store multiple key's on the same index, but may need to run a loop

Linear Probing: Open Addressing method
If there is a collision, we will look for the empty spot until we find one for new key

Separate chaining: Storing multple keys to the same address 
We are going to keep it as a list, but it can also be implemented with linked list

"""
#Big O 
# Insert and Look up by KEY in hash table is O(1)
# Lookup by a VALUE in hash table is O(n)
# Insert and lookup for BST is better because it is sorted

class HashTable:
    def __init__(self, size=7):
        self.data_map = [None] * size
    
    def hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter)) *23 # any prime number can be used to multiply with ASCII number of the letter
        return my_hash % len(self.data_map)
    
    def print_table(self):
        for i,val in enumerate(self.data_map):
            print(i,":", val)
    
    def set_item(self, key, value):
        index = self.hash(key)
        if self.data_map[index] is None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])

    def get_item(self,key):
        index = self.hash(key)
        if self.data_map[index] is not None:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1] # This returns the value
        return None       

    #To take all keys in hashtable and put it into a list
    def find_keys(self):
        all_keys = []
        for i in range(len(self.data_map)):
            if self.data_map[i] is not None:
                for j in range(len(self.data_map[i])): #This is to loop through the elements in index
                    all_keys.append(self.data_map[i][j][0])
        return all_keys   

my_hash_table = HashTable()
my_hash_table.set_item('bolts', 1200)
my_hash_table.set_item('washer', 1300)
my_hash_table.set_item('pipes', 1100)
print("Get Item:") 
print(my_hash_table.get_item('washer'))
print("Keys:")
print(my_hash_table.find_keys())
print("Hash Table:") 
my_hash_table.print_table()
