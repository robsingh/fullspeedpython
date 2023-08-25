"""Chapter - 10 Generators"""

# def myrange(a,b):
#     while a < b:
#         yield a
#         a += 1

# for value in myrange(1,5):
#     print(value)


# def squares(n):
#     for value in range(n):
#         yield value * value


# for value in squares(4):
#     print(value)


"""Implement a generator called “squares” to yield the square of all numbers from (a)
to (b). Test it with a “for” loop and print each of the yielded values."""

# def squares(a,b):
#     for value in range(a,b+1):
#         yield value * value

# for value in squares(1,5):
#     print(value)


"""Create a generator to yield all the even numbers from 1 to (n)"""

# def gen_even(a,n):
#     for i in range(a,n):
#         if i % 2 == 0:
#             yield i


# for value in gen_even(1,10):
#     print(value)
    

"""Create another generator to yield all the odd numbers from 1 to (n)"""

# def odd_gen(a,n):
#     for i in range(1,n):
#         if i % 2 != 0:
#             yield i


# for value in odd_gen(1,10):
#     print(value)

"""Implement a generator that returns all numbers from (n) down to 0."""

# def ret_all(n):
#     if n < 0:
#         raise StopIteration
#     else:
#         for i in range(n):
#             yield n
#             n -= 1


# for value in ret_all(5):
#     print(value)


"""Create a generator to return the fibonnaci sequence starting from the first element
up to (n). The first numbers of the sequence are: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55,
89, . """

# def fib(n):
#     prev = 0
#     curr = 1
#     while prev < n:
#         yield prev
#         prev,curr = curr, prev+curr
            

# for value in fib(20):
#     print(value)

"""
Implement a generator that returns all consecutive pairs of numbers from 0 to (n),
such as (0, 1), (1, 2), (2, 3). . .
"""

def consec_pairs(n):
    for i in range(n):
        yield i, i+1
    
for value in consec_pairs(5):
    print(value)