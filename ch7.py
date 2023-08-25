"""Chapter - 7 Dictionaries"""

ages = {
"Peter": 10,
"Isabel": 11,
"Anna": 9,
"Thomas": 10,
"Bob": 10,
"Joseph": 11,
"Maria": 12,
"Gabriel": 10,
"chuck": 19
}

# How many students are in the dictionary
# print(len(ages))

"""
Implement a function that receives the “ages” dictionary as parameter and returns
the average age of the students. Traverse all items on the dictionary using the
“items” method as above.
"""

# def avg_age(ages):
#     total_age = 0
#     total_students = len(ages)

#     for student, age in ages.items():
#         total_age += age

#     avg_age = total_age/total_students
#     return avg_age


# print(avg_age(ages))

"""
Implement a function that receives the “ages” dictionary as parameter and returns
the name of the oldest student.

Consider the case if the two or more students have same age and they are oldest.
"""

# def oldest_student(ages):
#     if not ages:
#         return []
#     max_value = ages[next(iter(ages))]

#     for value in ages.values():
#         if value > max_value:
#             max_value = value

#     max_items = {key: value for key, value in ages.items() if value == max_value}
#     return max_items


# max_items = oldest_student(ages)
# print("Oldest student is:  ")

# for key,value in max_items.items():
#     print(key)


"""
Implement a function that receives the “ages” dictionary and a number “n” and
returns a new dict where each student is (n) years older. For instance, new_ages(ages,
10) returns a copy of “ages” where each student is 10 years older.
"""

# def ages_n(ages,n):
#     ages_dict = {}
#     for name,age in ages.items():
#         if age == n:
#             ages_dict[name] = n
#     return ages_dict

# n = 10
# print(f"{n} year older student is: ",ages_n(ages,10))

# def new_ages(ages,n):
#     new_ages_dict = {}
#     for name,age in ages.items():
#         new_age = age + n
#         new_ages_dict[name] = new_age
#     return new_ages_dict

# n = 10
# print(f"{n} year old student is: ",new_ages(ages,10))


students = {
"Peter": {"age": 10, "address": "Lisbon"},
"Isabel": {"age": 11, "address": "Sesimbra"},
"Anna": {"age": 9, "address": "Lisbon"},
}

"""
How many students are in the “students” dict? Use the appropriate function
"""
# print(len(students))

"""
Implement a function that receives the students dict and returns the average age.
"""
# def avg_age(students):
#     num_students = 0
#     total_age = 0
#     for student in students.values():
#         total_age += student["age"]
#         num_students += 1
        

#     average = total_age / num_students
#     return average

# print(avg_age(students))


"""
Implement a function that receives the students dict and an address, and returns a
list with names of all students whose address matches the address in the argument.
For instance, invoking “find_students(students, ’Lisbon’)” should return Peter and
Anna.
"""
# students = {
# "Peter": {"age": 10, "address": "Lisbon"},
# "Isabel": {"age": 11, "address": "Sesimbra"},
# "Anna": {"age": 9, "address": "Lisbon"},
# }

# def find_students(students, address_arg='Lisbon'):
#     for student in students:
#         if students[student]['address'] == address_arg:
#             print(f"Students whose address matches are: {student}")
        

# (find_students(students, address_arg='Lisbon'))

# def find_students(students, address):
#     matching_students = []
#     for name, info in students.items():
#         if info['address'] == address:
#             matching_students.append(name)  #in case you want a dictionary with all details, do -> append({name:info})
#     return matching_students

# print(find_students(students, address='Lisbon'))
