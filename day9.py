#Write a program to sort a list of numbers in ascending order using Bubble Sort.

def bubble_sort(numbers):  #solution
    n = len(numbers)
    for i in range(n):
        # Traverse through the list
        for j in range(0, n - i - 1):
            # Swap if the current element is greater than the next
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

# List to be sorted
numbers = [64, 34, 25, 12, 22, 11, 90]

bubble_sort(numbers)
print("Sorted List:", numbers)

#Modify Bubble Sort to sort a list in descending order.


def bubble_sort_desc(numbers):  #solution
    n = len(numbers)
    for i in range(n):
        for j in range(0, n - i - 1):
            # Swap if the current element is smaller than the next
            if numbers[j] < numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

# List to be sorted
numbers = [5, 1, 4, 2, 8]

bubble_sort_desc(numbers)
print("Sorted List in Descending Order:", numbers)

#Use Bubble Sort to sort a list of strings in alphabetical order.


def bubble_sort_strings(strings): #solution
    n = len(strings)
    for i in range(n):
        for j in range(0, n - i - 1):
            # Compare strings lexicographically
            if strings[j] > strings[j + 1]:
                strings[j], strings[j + 1] = strings[j + 1], strings[j]

# List of strings
strings = ["banana", "apple", "cherry", "date"]

bubble_sort_strings(strings)
print("Sorted Strings:", strings)

#Modify Bubble Sort to count the number of swaps performed during sorting.


def bubble_sort_count(numbers): #solution
    n = len(numbers)
    swap_count = 0
    for i in range(n):
        for j in range(0, n - i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
                swap_count += 1
    print("Number of swaps:", swap_count)

# List to be sorted
numbers = [3, 2, 1]

bubble_sort_count(numbers)

#Modify Bubble Sort to terminate early if the list is already sorted.


def optimized_bubble_sort(numbers): #solution
    n = len(numbers)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
                swapped = True
        # Break out if no swaps occurred
        if not swapped:
            break

# List to be sorted
numbers = [1, 2, 3, 4, 5]

optimized_bubble_sort(numbers)
print("Optimized Bubble Sort Result:", numbers)