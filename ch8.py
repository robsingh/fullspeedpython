"""Chapter - 8 Classes"""

"""
Implement a class named “Rectangle” to store the coordinates of a rectangle given
by (x1, y1) and (x2, y2).

I did additional thing to calculate the area, but it was not the ask.
"""
# class Rectangle:
#     def __init__(self,x1,y1,x2,y2):
#         self.x1 = x1
#         self.y1 = y1
#         self.x2 = x2
#         self.y2 = y2

#     def area(self):
#         width = abs(self.x2 - self.x1)
#         height = abs(self.y2 - self.y1)
#         area = width * height
#         return area


# rect = Rectangle(0,0,5,5)
# area_rect = rect.area()
# print(area_rect)
    

"""
Implement the “width()” and “height()” methods which return, respectively, the
width and height of a rectangle. Create two objects, instances of “Rectangle” to
test the calculations.
"""

# class Rectangle:
#     def __init__(self,x1,y1,x2,y2):
#         self.x1 = x1
#         self.y1 = y1
#         self.x2 = x2
#         self.y2 = y2

    
#     def width(self):
#         return abs(self.x2 - self.x1)
    
#     def height(self):
#         return abs(self.y2 - self.y1)
    


# rec1 = Rectangle(0,0,5,5)
# rec2 = Rectangle(3,3,8,10)

# print(f"Width of Rec 1: {rec1.width()} cm")
# print(f"Height of Rec 1: {rec1.height()} cm")
# print(f"Width of Rec 2: {rec2.width()} cm")
# print(f"height of Rec 2: {rec2.height()} cm")

"""
Implement the method “circumference” to return the perimeter of the rectangle
(2*width + 2*height).

Do a print of one of the objects created to test the class. Implement the “__str__”
method such that when you print one of the objects it print the coordinates as (x1,
y1)(x2, y2).
"""

# class Rectangle:
#     def __init__(self,x1,y1,x2,y2):
#         self.x1 = x1
#         self.y1 = y1
#         self.x2 = x2
#         self.y2 = y2

#     def circumference(self):
#         width = abs(self.x2 - self.x1)
#         height = abs(self.y2 - self.y1)
#         perimeter = (2*width + 2*height)
#         return perimeter
    
#     def __str__(self):
#         return "({},{})({},{})".format(self.x1,self.y1,self.x2,self.y2)
    


# rec = Rectangle(3,3,8,10)
# print("Printing coordinates as requested: ",rec)
# print(f"Perimeter of rectangle is: {rec.circumference()}cm")

