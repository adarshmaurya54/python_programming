# Question:
# You are given a tuple numbers = (10, 5, 2, 8, 7, 5, 10, 3). Perform the following operations:
# 1. Count the number of occurrences of the number 5 in the tuple.
# 2. Find the index of the first occurrence of the number 7 in the tuple.
# 3. Create a new tuple by concatenating numbers with another tuple extra_numbers = (4, 6).
# 4. Sort the elements of the tuple in ascending order.
# 5. Remove duplicates from the tuple and return a new tuple with unique values.
# 6. Reverse the tuple.

numbers = (10, 5, 2, 8, 7, 5, 10, 3)
extra_numbers = (4, 6)

count_five = numbers.count(5)
print("Number of 5s:", count_five)

index_seven = numbers.index(7)
print("Index of 7:", index_seven)

concatenated = numbers + extra_numbers
print("Concatenated tuple:", concatenated)

sorted_numbers = tuple(sorted(numbers))
print("Sorted tuple:", sorted_numbers)

unique_numbers = tuple(sorted(set(numbers)))
print("Unique numbers:", unique_numbers)

reversed_numbers = tuple(reversed(numbers))
print("Reversed tuple:", reversed_numbers) 