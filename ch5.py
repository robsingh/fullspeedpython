#Chapter - 5 Modules and Functions
"""
Implement the “add2” function that receives two numbers as arguments and returns
the sum of the numbers. Then implement the “add3” function that receives and
sums 3 parameters.
"""

# def add2(num1,num2):
#     return num1 + num2

# def add3(num1,num2,num3):
#     return num1 + num2 + num3

# print(add2(10,10))
# print(add3(10,20,30))

"""
Implement a function that returns the greatest of two numbers given as parameters.
Use the “if” statement to compare both numbers
"""

# def greatest(num1,num2):
#     if num1 > num2:
#         return num1
#     return num2

# print(greatest(12,10))

"""
Implement a function named “is_divisible” that receives two parameters (named “a”
and “b”) and returns true if “a” can be divided by “b” or false otherwise. A number
is divisible by another when the remainder of the division is zero. Use the modulo
operator (“%”).
"""

# def is_divisible(a,b):
#     if a % b == 0:
#         return True
#     return False

# print(is_divisible(4,3))
# print(is_divisible(4,2))

"""
Create a function named “average” that computes the average value of a list passed
as parameter to the function. Use the “sum” and “len” functions.
"""

# def average(list):
#     avg = sum(list)/len(list)
#     return avg

# list = [45, 34, 10, 36, 12, 6, 80]
# print(round(average(list),2))

""" Recursive Functions"""
"Implement the factorial function and test it with several different values."

# def recursive(x):
#     if x == 0:
#         return 1
#     return x * recursive(x-1)

# print(recursive(10))


"""Implement a recursive function to compute the sum of the (n) first integer numbers
(where (n) is a function parameter). Start by thinking about the base case (the sum
of the first 0 integers is?) and then think about the recursive case."""


# def recur_sum(n):
#     if n <= 1:
#         return n
#     return n + recur_sum(n-1)


# print(recur_sum(5))


"""
The Fibonnaci sequence is a sequence of numbers in which each number of the
sequence matches the sum of the previous two terms. Given the following recursive
definition implement (fib(n)).
fib(n) =

0, if x = 0.
1, if x = 1.
fib(n − 1) + fib(n − 2), 

Check your results for the first numbers of the sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21,
34, 55, 89,
"""

# def fib_sum(n):
#     if n <= 1:
#         return n
#     return fib_sum(n-1) + fib_sum(n-2)


# print(fib_sum(11))