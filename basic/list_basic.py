# List operations
my_list = [1, 2, 3, 4, 5]
print("Original list:", my_list)

# Adding elements
my_list.append(6)
print("After append:", my_list)

# Inserting elements
my_list.insert(2, 2.5)
print("After insert:", my_list)

# Removing elements
my_list.remove(3)
print("After remove:", my_list)

# Slicing lists
sub_list = my_list[1:4]
print("Sub list:", sub_list)

# Sorting lists
my_list.sort()
print("Sorted list:", my_list)






# List comprehension
squared_list = [x**2 for x in my_list]
print("Squared list:", squared_list)
