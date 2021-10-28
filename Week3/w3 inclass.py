'''
file: w3 in class

'''
#string, int, float
x = '10.0'
y = 5
z = 3.14

#what is stored in a, b, c?
a = 10 + 4 * 2 - 3
b = 5 % 2
c = 7 // 2
print(a, b, c)

import math

#team activity
#square
side = float(input("What is the length of a side of square? "))
squ_area_cent = side * side
squ_area_meter = side * side/100
print(f"The area of the square is: {squ_area_cent}cm^2")
print(f"The area of the square is: {squ_area_meter/100}m^2")

#rectangle
length = float(input("What is the length of rectangle?"))
width = float(input("What is the width of rectangle?"))
rec_area = length * width
print(f"The area of the rectangle is: {rec_area}")
#circle
radius = float(input("What is the radius of circle?"))
cir_area = radius * 3.14
print(f"The area of the circle is: {cir_area}")

#stretch
value = float(input("What is the value for the area ?"))
cir_area = value * math.pi 
squ_area = value * value
cube_side = value **3
sphere_radius = (value**3 )*4/3 * math.pi
print(cir_area)
print(squ_area)
print(cube_side)
print(sphere_radius)

