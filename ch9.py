"""Chapter 9 - Iterators"""

"""Implement an iterator class to return the square of all numbers from “a” to “b”."""

# class SquareIterator:
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b
#         self.current = a

#     def __iter__(self):
#         return self
    

#     def __next__(self):
#         if self.current > self.b:
#             raise StopIteration
#         else:
#             square = self.current ** 2
#             self.current += 1
#             return square
        

# sq_iterator = SquareIterator(1,5)
# for square in sq_iterator:
#     print(square)


"""Implement an iterator class to return all the even numbers from 1 to (n)"""

# class EvenIterator:
#     def __init__(self,n):
#         self.n = n
#         self.current = 2

#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         if self.current > self.n:
#             raise StopIteration
#         else:
#             even_number = self.current
#             self.current += 2
#             return even_number


# even_iterator = EvenIterator(5)
# for even in even_iterator:
#     print(even)

"""Implement an iterator class to return all the odd numbers from 1 to (n)"""

# class OddIterator:
#     def __init__(self,n):
#         self.n = n
#         self.current = 1

#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         if self.current > self.n:
#             raise StopIteration
#         else:
#             odd_number = self.current
#             self.current += 2
#             return odd_number
        
# odd_iterator = OddIterator(10)
# for odd in odd_iterator:
#     print(odd)

""" Implement an iterator class to return all numbers from (n) down to 0"""

# class meterDown:
#     def __init__(self,n):
#         self.n = n
#         self.current = n

#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         if self.current < 0:
#             raise StopIteration
#         else:
#             dep_num = self.current
#             self.current -= 1
#             return dep_num
        
# all_num = meterDown(4)
# for num in all_num:
#     print(num)


"""Implement an iterator class to return the fibonnaci sequence from the first element
up to (n).These are the first numbers of the sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34,
55, 89, . . ."""

# class fibonaacii:
#     def __init__(self,n):
#         self.n = n
#         self.prev = 0
#         self.current = 1

#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         if self.prev + self.current > self.n:
#             raise StopIteration
#         else:
#             num = self.prev + self.current
#             self.prev = self.current
#             self.current = num
#             return num
        

# fibo = fibonaacii(10)
# for num in fibo:
#     print(num)

"""Implement an iterator class to return all consecutive pairs of numbers from 0 until
(n), such as (0, 1), (1, 2), (2, 3). ."""


class allPairs:
    def __init__(self,n):
        self.n = n
        self.currrent = 0

    def __iter__(self):  #returning instance of the class, class itself is iterable
        return self
    
    def __next__(self):
        if self.currrent >= self.n:
            raise StopIteration
        else:
            pair = (self.currrent, self.currrent+1)
            self.currrent += 1
            return pair
        
consec_pairs = allPairs(5)
for pairs in consec_pairs:
    print(pairs)
