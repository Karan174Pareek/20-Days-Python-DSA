#Write a program to find the index of the first occurrence of a specific element in a tuple.

# Define a tuple
my_tuple = ("apple", "banana", "cherry", "apple") #solution

# Find index of "cherry"
index = my_tuple.index("cherry")

# Print result
print("Index of 'cherry':", index)


#Write a program to calculate the number of elements in a tuple.


my_tuple = (1, 2, 3, 4, 5) #solution

# Find length
length = len(my_tuple)

# Print result
print("Length of the tuple:", length)

#Write a program to count how many times a specific element appears in a tuple.

# Define a tuple
my_tuple = (1, 2, 3, 2, 4, 2, 5) #solution

# Count occurrences of 2
count = my_tuple.count(2)

# Print result
print("Number 2 appears", count, "times in the tuple.")

#Write a program to create a tuple with mixed data types and access its elements using indexing and slicing.

# Defining a tuple with mixed data types
my_tuple = (10, "Python", 3.14, True) #solution

# Access elements using indexing
print("First element:", my_tuple[0])
print("Second element:", my_tuple[1])

# Access elements using slicing
print("Sliced tuple:", my_tuple[1:3])

#Write a program to unpack the elements of a tuple into separate variables.


# Define a tuple
my_tuple = (10, 20, 30) #solution

# Unpack tuple
a, b, c = my_tuple

# Print unpacked values
print("a:", a)
print("b:", b)
print("c:", c)