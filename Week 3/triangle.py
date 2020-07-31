# s=(a+b+c)/2
# Area=sqrt(s*(s-a)*(s-b)*(s-c))

# take inputs for a,b,c
# perform computation: Area
# output the lengths and area

import math

a = int(input("Enter the length of the first side: "))
b = int(input("Enter the length of the second side: "))
c = int(input("Enter the length of the third side: "))

s = (a + b + c)/2

area = math.sqrt(s*(s-a)*(s-b)*(s-c))

# output the lengths and area
print("The area of the triangle with sides of length", a, "and", b, "and", c, "is", str(area)+".")
