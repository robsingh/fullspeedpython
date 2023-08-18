"""
A leap year is a calendar year containing an additional day added to keep the calendar year synchronized with the astronomical or seasonal year. 
In the Gregorian calendar, each leap year has 366 days instead of 365, by extending February to 29 days rather than the common 28. 
These extra days occur in years which are multiples of four (with the exception of centennial years not divisible by 400). 
Write a Python program, which asks for a year and calculates, if this year is a leap year or not.
"""
"""
condition for leap year:
1. feb has 29 days
2. multiple of 4 and exception of year not divisible by 400
"""
def leap_year(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return f'{year} is a leap year'
    else:
        return f'{year} is not a leap year!!'



year = int(input("Enter a year: "))
print(leap_year(year))