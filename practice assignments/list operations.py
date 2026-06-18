from functools import reduce

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# map() - Square of each number
squares = list(map(lambda x: x * x, numbers))

# filter() - Even numbers
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

# reduce() - Sum of all numbers
total = reduce(lambda x, y: x + y, numbers)

print("Original List:", numbers)
print("Squares using map():", squares)
print("Even Numbers using filter():", even_numbers)
print("Sum using reduce():", total)
