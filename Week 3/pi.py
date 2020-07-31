

#round function to display the computed values with 3 decimal places e.g. round(5.23517, 3) is 5.235.

#Sample I/O:

#Approximation of pi: 3.142 Enter the radius:

#2.5

#Area: 19.635

from math import sqrt

root = 2*(2/sqrt(2))
denominator = sqrt(2)
pi = root


while 2 / sqrt(2 + denominator) > 1:
    pi = pi * 2 / sqrt(2 + denominator)
    denominator = sqrt(2 + denominator)
print("Approximation of pi: %s" % (round(pi, 3)))

r = float(input ("Enter the radius : "))
area = pi * r **2

print ("Area: " + str(round(area,3)))
