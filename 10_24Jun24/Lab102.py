# Filter in Python

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# filter is similar to map

def isEven(num):
    return num % 2 == 0


new_numbers_even = filter(isEven, numbers)
print(list(new_numbers_even))


def is_Greater_5(num):
    return num > 5

greater_five = filter(is_Greater_5, numbers)
print(list(greater_five))