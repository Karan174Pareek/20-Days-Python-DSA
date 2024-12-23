#Write a program to create a dictionary of a student's details and access specific values.

# Creating a dictionary
student = {"name": "John", "age": 20, "major": "Computer Science"} #solution

# Access values
print("Name:", student["name"])
print("Age:", student.get("age"))

#Write a program to count how many times each element appears in a list.

# Define a list
numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4] #solution

# Create a frequency dictionary
frequency = {}
for num in numbers:
    frequency[num] = frequency.get(num, 0) + 1

# Print frequency dictionary
print("Frequency of numbers:", frequency)

#Write a program to iterate through a dictionary and print all key-value pairs.


fruit_prices = {"apple": 100, "banana": 50, "cherry": 200} #solution

# Iterate through the dictionary
for fruit, price in fruit_prices.items():
    print(f"The price of {fruit} is {price}")

    #Write a program to remove a key-value pair from a dictionary.


person = {"name": "Alice", "age": 30, "city": "London"} #solution

# Remove a key-value pair
removed_value = person.pop("city")

# Print updated dictionary and removed value
print("Updated Dictionary:", person)
print("Removed Value:", removed_value)

#Write a program to add a new key-value pair to a dictionary and update an existing key.


student = {"name": "Jeet", "age": 18} #solution

# Add a new key-value pair
student["major"] = "Python Programming"

# Update an existing key
student["age"] = 19

# Print updated dictionary
print("Updated Student Dictionary:", student)