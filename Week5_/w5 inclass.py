'''
File:w5 inclass
'''

#if condition1:
#if = keyword, : means there are code block follow
#for true or false
#can stand alone

#elif condition2:
#use elif when the 2nd answer is true

#else:
#excute if all condition are false

#decision, decision, decision
a = 5
b = 10 

if a < b:
    print('a is less than b')
elif a == 15:
    print('a is 15')
else:
    print('a is not less than b or equal to 15')

#compare in list
my_list = [1,2,5,10]
if a in my_list:
    print('a is in the list')

#operator or, and, not
#  

#team activity
#CORE REQUIREMENTS
print('Hi, Welcome to automatic grade calculation')
grade = int(input(f"What grade do you get? "))
'''
if grade >= 90:
    print("You got A!")
elif grade >= 80:
    print("You got B!")
elif grade >= 70:
    print("You got C!")
elif grade >= 60:
    print("You got D!")
else:
    print("You got F. You tried, but you can do better on next time")
print()
if grade >= 70:
    print("You passed!")
else:
    print("You did not pass for this class. Please try again! You got this!")

'''

#STRETCH CHALLENGE
if grade >= 90:
    letter = "A"
if grade >= 80: 
    letter = "B"
elif grade >= 70:
    letter = "C"
elif grade <= 60:
    letter = "D"

print()
if grade%10 >=7:
    sign = "+"
elif grade%10 <3:
        sign = "-"
else:
    sign = ""

if grade >= 93:
    sign = ""
if letter == "F":
    sign = ""

print(f"You got {letter}{sign}. ")


if grade >= 60:
    print("Good job!")
else: 
    print("Try one more time. You can do it!")


