#Use Selection Sort logic to find the k-smallest element in a list.


def find_k_smallest(numbers, k):  #solution
    n = len(numbers)
    for i in range(k):
        min_index = i
        for j in range(i + 1, n):
            if numbers[j] < numbers[min_index]:
                min_index = j
        numbers[i], numbers[min_index] = numbers[min_index], numbers[i]
    return numbers[k - 1]

# List and k value
numbers = [7, 10, 4, 3, 20, 15]
k = 3

k_smallest = find_k_smallest(numbers, k)
print(f"The {k}-smallest element is:", k_smallest)

#Write a program to sort a list of numbers in ascending order using Selection Sort.

def selection_sort(numbers): #solution
    n = len(numbers)
    for i in range(n):
        # Find the minimum element in the remaining unsorted part
        min_index = i
        for j in range(i + 1, n):
            if numbers[j] < numbers[min_index]:
                min_index = j
        # Swap the found minimum with the first element of the unsorted part
        numbers[i], numbers[min_index] = numbers[min_index], numbers[i]

# List to be sorted
numbers = [64, 25, 12, 22, 11]

selection_sort(numbers)
print("Sorted List:", numbers)

#Modify Selection Sort to count the number of comparisons performed during sorting.


def selection_sort_count(numbers):  #solution
    n = len(numbers)
    comparison_count = 0
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            comparison_count += 1
            if numbers[j] < numbers[min_index]:
                min_index = j
        numbers[i], numbers[min_index] = numbers[min_index], numbers[i]
    print("Number of comparisons:", comparison_count)

# List to be sorted
numbers = [3, 1, 2, 4]

selection_sort_count(numbers)

#Modify Selection Sort to sort a list in descending order.


def selection_sort_desc(numbers): #solution
    n = len(numbers)
    for i in range(n):
        # Find the maximum element in the remaining unsorted part
        max_index = i
        for j in range(i + 1, n):
            if numbers[j] > numbers[max_index]:
                max_index = j
        # Swap the found maximum with the first element of the unsorted part
        numbers[i], numbers[max_index] = numbers[max_index], numbers[i]

# List to be sorted
numbers = [20, 12, 10, 15, 2]

selection_sort_desc(numbers)
print("Sorted List in Descending Order:", numbers)

#Use Selection Sort to sort a list of strings in alphabetical order.


def selection_sort_strings(strings):  #solution
    n = len(strings)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if strings[j] < strings[min_index]:
                min_index = j
        strings[i], strings[min_index] = strings[min_index], strings[i]

# List of strings
strings = ["banana", "apple", "cherry", "date"]

selection_sort_strings(strings)
print("Sorted Strings:", strings)