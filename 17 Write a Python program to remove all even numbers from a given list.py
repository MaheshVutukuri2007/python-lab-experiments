# Original list with mixed numbers
numbers = [12, 7, 9, 14, 5, 20, 3, 8, 11]

# Using list comprehension to filter only odd numbers
odd_numbers = [num for num in numbers if num % 2 != 0]

# Output
print("Original List:", numbers)
print("List after removing even numbers:", odd_numbers)
