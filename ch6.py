# """Chapter 6 Iteration and Loops"""

# """Create a function “add” that receives a list as parameter and returns the sum of all
# elements in the list. Use the “for” loop to iterate over the elements of the list."""

# # def add_to(list):
# #     sum = 0
# #     for i in list:
# #         sum += i
# #     return sum


# # print(add_to(list=[1,2,3,4]))

"""
Create a function that receives a list as parameter and returns the maximum value
in the list. As you iterate over the list you may want to keep the maximum value
found so far in order to keep comparing it with the next elements of the list.
"""


# def find_max(arr):
#     max_value = arr[0]
#     for element in arr[1:]:
#         if element > max_value:
#             max_value = element
#     return max_value


# arr = [1,2,3,4]
# print(find_max(arr))

"""
Modify the previous function such that it returns a list with the first element being
the maximum value and the second being the index of the maximum value in the
list. Besides keeping the maximum value found so far, you also need to keep the
position where it occurred.

"""
# def find_max(arr):
#     max_element = arr[0]
#     for key,value in enumerate(arr[1:]):
#         if value > max_element:
#             max_element = value
        
#     print('max_value is :', max_element, 'and key is:',key)
#     # return max_element, key


# (find_max(arr=[1,2,356,7]))


"""
Implement a function that returns the reverse of a list received as parameter.
You may create an empty list and keep adding the values in reversed order as
they come from the original list.
"""

# def reverse_func(arr):
#     reverse_list = []
#     for i in range(len(arr)):
#         reverse_list.append(arr[len(arr)-1-i])
#     return reverse_list
# arr[::-1] -> another shortcut

# print(reverse_func(arr=[1,2,3,4,5]))


"""
Make the function “is_sorted” that receives a list as parameter and returns True if
the list is sorted in ascending order. For instance [1, 2, 2, 3] is ordered while [1, 2, 3,
2] is not. Suggestion: you have to compare a number in the list with the next one,
so you can use indexes or you need to keep the previous number in a variable as
you iterate over the list.
"""

# def is_sorted(arr):
#       for i in range(len(arr)-1):
#         if arr[i] > arr[i+1]:
#             return False
#       return True




# print(is_sorted(arr=[1,2,3,4,2]))
# print(is_sorted(arr=[1,2,2,3]))


"""
Implement the function “is_sorted_dec” which is similar to the previous one but
all items must be sorted by decreasing order
"""

# def is_sorted_dec(arr):
#     for i in range(len(arr)-1):
#         if arr[i] < arr[i+1]:
#             return False
#     return True

# print(is_sorted_dec(arr=[1,2,3,4,3,2]))
# print(is_sorted_dec(arr=[1,2,3,4]))


"""
Implement the “has_duplicates” function which verifies if a list has duplicate values.
You may have to use two “for” loops, where for each value you have to check for
duplicates on the rest of the list.
"""

# def has_duplicates(arr):
#     for i in range(len(arr)):
#         for j in range(i+1, len(arr)):
#             if arr[i] == arr[j]:
#                 return True
#     return False
        

# print(has_duplicates(arr=[1,2,2,3,4]))

# another way - efficient one

# def has_duplicates(arr):
#     seen = set()
#     for item in arr:
#         if item in seen:
#             return True
#         seen.add(item)
#     return False


"""
Implement a function that receives a number as parameter and prints, in decreasing 
order, which numbers are even and which are odd, until it reaches 0.

"""

# def even_odd(num):
#     while num >= 0:
#         if num % 2 == 0:
#             print(f"{num} is even ")
#             num -= 1
#         else:
#             print(f"{num} is odd ")
#             num -= 1

# print(even_odd(10))

 