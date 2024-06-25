# Leetcode - Sum of Digits [Recursive Program]

number = 12345
sum_of_digits = 15

number = int(input("Enter a number: "))
def sum_of_digits(n):
    # Base Class
    if n < 10:
        return n
    # Recursive Class
    else:
        return n % 10 + sum_of_digits(n // 10)

result = sum_of_digits(number)
print(result)