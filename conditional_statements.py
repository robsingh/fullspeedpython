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
# def leap_year(year):
#     if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
#         return f'{year} is a leap year'
#     else:
#         return f'{year} is not a leap year!!'



# year = int(input("Enter a year: "))
# print(leap_year(year))

"""
Body mass index (BMI) is a value derived from the mass (weight) and height of a person. 
The BMI is defined as the body mass divided by the square of the body height, and is universally expressed in units of kg/m2, 
resulting from mass in kilograms and height in metres. $ BMI = \frac{m}{l^{2}}$ 
Write a program, which asks for the length and the weight of a person and returns an evaluation string
"""

height = float(input("What is your height? "))
weight = float(input("What is your weight? "))

bmi = weight/height ** 2
print(bmi)

if bmi < 15:
    print("Very severly underweight")
elif bmi < 16:
    print("Severly underweight")
elif bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal (healthy) weight")
elif bmi < 30:
    print("Overweight")
elif bmi < 35:
    print("Obese Class I (Moderately obese)")
elif bmi < 40:
    print("Obese Class II (Severly obese)")
else:
    print("Obese Class III (Very Severly Obese)")

    