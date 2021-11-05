'''
file: W5 prepare activity
BASIC FRAMEWORK

'''
#basic framework for "if statements," or conditional statements
if condition:
    then-stuff-goes-here
#4 spaces not a tab

#if the condition is not true, then we can list other things in
# the "else" clause like this
if condition:
    then-stuff-goes-here
else:
    the-otherwise-stuff-goes-here

#COMPARING STRINGS
color = input("What is your favorite color? ")
# This if statement will only match "blue" not "Blue" or "BLUE"
if color == "blue":
    print("I like blue too.")

# This if statement will match the word blue, regardless of the capitalization
if color.lower() == "blue":
    print("I like blue too.")
