'''
flie: w6 inclass (and booleans and complex condition)
'''
'''
#boolean variable can be assign directily
can_

#note a good variable name will indicate that it only has two possible values(t/f)

#logical operators-see table
#bbecareful with complex condition(ones with and/or)
x = 4
y= x == 5 or 2
print(f"{y=}")

#better way 
x = 4
y = x==5 or x==2

#logical have an order of operation too
meal = "sandwich"
money = 0
if (meal == "sandwich" or meal == "pizza") and money > 5:
    print("your order will be ready in five mins")
'''

'''
team activity
'''
age1 = float(input("What is the age of the first rider? "))
height1 = float(input("What is the height of the first rider? "))
if height1<36 :
    can_ride = False
elif age1 >= 18 and height1 >= 62:
    can_ride = True
else:
    if age1 >= 12 and age1 <= 17 and height1 >=52 :
        golden_passport = input("Do you have golden passport(yes or no)?")
        if golden_passport.lower() == "yes":
            can_ride = True
        if golden_passport.lower() == "no":
            can_ride = False
    else:
        second = input("Is there a second rider(yes/no)? ")

        if second.lower() == 'yes':
            can_ride = True
            age2 = float(input("What is the age of the second rider? "))
            height2 = float(input("What is the height of the second rider? "))
            if height1<36 :
                can_ride = False
            elif age2 >= 18 and height2 >= 62:
                can_ride = True
            else:
                if (age1 >= 18 and age2 >= 18 )and height1 >= 52 and height2 >= 52:
                    can_ride = True
                if (age1 >= 12 or age2 >= 12 ) and age1 <= 17 or age2 <= 17:
                    golden_passport = input("Do you have golden passport(yes or no)?")
                    if golden_passport.lower() == "yes":
                        can_ride = True        
        else:
            can_ride = False

if can_ride:
    print("Go have fun!")
else:
    print("Go home.")

