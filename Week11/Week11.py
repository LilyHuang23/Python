'''
File: Week 11 in class & Team activity
Topic: open file and use strip & split
'''
# Opening and reading from files in Python
file = open("files.txt")
file.close()

# close and open together
with open("files.txt") as file:
    for line in file:
        print("line")
# .strip Removing extra whitespace

#clean_line = old_line.strip()

# Splitting a string into pieces
sentence = "I will go and do"

words = sentence.split(" ")
# The variable "words" is now a list that contains each word.

# You can iterate through each word and do something with it, such as display it:
for word in words:
    print(word)

# Team activity
with open("hr_system.txt") as employee_info:
    for line in employee_info:
        clean_line = line.strip()
        line_list = clean_line.split(" ")
        print(f"Name:{line_list[0]},Title:{line_list[2]}")
# Stretch Challenge
with open("hr_system.txt") as employee_info:
    for line in employee_info:
        clean_line = line.strip()
        line_list = clean_line.split(" ")
        name = line_list[0]
        id = line_list [1]
        title = line_list [2]
        salary = line_list[3]
        print(f"{name} (ID: {id}), {title} - ${salary}")