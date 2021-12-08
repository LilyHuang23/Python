'''
File: Week 13 in class & Team activity
Topic: funcation
'''
#inclass
#def = define, keyword
#description of what the funtion does
#paramenter, if you need data outside of this file
#return = keyword
#output = result


#def function_name(prarmenter):
    #'''doc string (explain the function)'''
    #code block e.g. for loop, if steatment...
    ##return output

import math
#team activity
kinds_of_shape = [["Square"],["Rectangle"],["Circle"]]
for shape in kinds_of_shape:
    print("Please input the number or type 'quit' to quit.")
    shape_question = (input("What kinds of shape you would like to compute?\n1.Square\n2.Rectangle\n3.Circle\n"))
    if shape_question == "1":
        def compute_area_square(side):
            '''compute the area of the square:
            params:
            side: the length of one side of output:
            area of the square'''
            area = side * side
            return area #side**2

        side_of_square = float(input("What is the length of a side of the square? "))

        area_of_square = compute_area_square(side_of_square)
        print(area_of_square)
    elif shape_question =="2":
        def compute_area_rectangle(length,width):
            rentangle_area = length * width
            return rentangle_area 
        side_of_length = float(input("What is the length of rectangle? "))
        side_of_width = float(input("What is the width of the rectangle? "))

        area_of_rentangle = compute_area_rectangle(side_of_length,side_of_width)
        print(area_of_rentangle)
    elif shape_question =="3":
        def compute_area_circle(radius):
            circle_area = 3.14 *(radius ** 2)
            return circle_area
        radius_of_circle = float(input("What is the radius of the circle? "))
        area_of_circle = compute_area_circle(radius_of_circle)
        print(area_of_circle)

    elif shape_question == "quit":
        print("Thank you!")
    else:
        print("Sorry, I don't understand")
# inclass 2
def say_hello(name1, name2,name3 = "beca"):
    print(f"hello{name1},{name2},{name3} how are you?")

var = say_hello(name3 = "john",name2 = "lily", name3 = "andy")
#it is ok not line up by the order, it will print follow by line60 
print(var)

#function memory
#inside the global memory
##global memory
#

