# Recursion: A programming technique in which function calls itself to solve a problem

# Key Concepts
# 1. BAse Case
# 2. Recursive Case


#Factorial
def factorial(n):
    # Base Case:
    if n == 0 or n == 1:
        return 1

    # Recursive Case:
    else:
        return n * factorial(n - 1)


print(factorial(5))

