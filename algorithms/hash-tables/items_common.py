# This is a common interview question to find matching elements in two list

list_1 = [1, 3, 5]
list_2 = [2, 4, 5]

#This has the O(n square)
def item_common_in_list_inefficient(list_1, list_2):
    for i in list_1:
        for j in list_2:
            if i == j:
                return True
    return False

print(item_common_in_list_inefficient(list_1, list_2))

#Efficient method id to use hash table which has O(n) as worst case
#Logic: Create a dict, store all keys with value as True, Compare elements of list 2 with the dict
def item_common_in_list_hash(list_1, list_2):
    my_dict = {}
    for i in list_1:
        my_dict[i] = True
    for j in list_2:
        if j in my_dict:
            return True
    return False

print(item_common_in_list_hash(list_1, list_2))


