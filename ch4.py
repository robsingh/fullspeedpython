#chapter - 4 Lists
# l = [1,4,9,10,23]

# sub_1 = l[1:3]   #4,9
# print(sub_1)

# sub_2 = l[3:]     #10,23
# print(sub_2)

# end = l.append(90)
# print(l)

# #average of everything
# total = sum(l)
# avg = total/len(l)
# print("avg is : ",format(avg,".2f"))

# #remove [4,9]
# l = [1,4,9,10,23]
# del l[1:3]
# print(l)

#List Comprehension
# create a list with the squares of the first 10 numbers.
# print([x * x for x in range(11)])

#  create a list with the cubes of the first 20 numbers.
# print([x*x*x for x in range(21)])

# all the even numbers from 0 to 20, and another one with all the odd numbers.
# print([x for x in range (0,21) if x % 2 == 0])
# print([x for x in range(0,21) if x % 2 != 0])

# Create a list with the squares of the even numbers from 0 to 20, and sum the list
# using the “sum” function. The result should be 1140. First create the list using list
# comprehensions, check the result, then apply the sum to the list comprehension.
# print(sum([(x * x) for x in range(0,20) if x % 2 == 0]))

# Make a list comprehension that returns a list with the squares of all even numbers
# from 0 to 20, but ignore those numbers that are divisible by 3. In other words,
# each number should be divisible by 2 and not divisible by 3. Search for the “and”
# keyword in the Python documentation. The resulting list is [4, 16, 64, 100, 196,
# 256]
# print([x * x for x in range(0,20) if x % 2 == 0 and x % 3 != 0])