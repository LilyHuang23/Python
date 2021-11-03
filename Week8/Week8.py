'''
file: w8 "for loop"


keyword /name you want/ keyword/ can be list. tuple,range, dictionary, string, ect
for variable in collection:

#use range to create collection
#built in funtion
range(start, stop, step)


# 1) loop to print 1 through 5
for x in [1,2,3,4,5]:
  print(x)
for x in range(1,6):
  print(x)
  
# 2) loop to do something a user specified number of times
#print()
user_input = int(input("how many times should it repeat: "))
for _ in range (user_input):  
  print("hi")
# 3) loop to print each letter in a string
print()
my_string = "have a nice day."
for character in my_string:
  print(character, end=" ")
  print()
  print("howdy")
# 4)loop to print each item in a list
print()
my_list = [1,2,3,4,5,6]
for x in my_list:
  print(x)
  
  
# team_activity
#Nested for loops
#pay attention at outter loop and inner loop, it will cause different result
# example
for i in range(1,5):
    print("i loop: ", i)
    for j in range(6,9):
        print("j loop: ", j, end=" ")
    print()
'''
#start

table = int(input("How many columns and rows do you want in your multiplication table? \n"))
range_size = table + 1
#biggest = table ** 2
#biggest = str(biggest)
#width = 
for row_number in range(1, range_size):
    for col_number in range(1, range_size):
        #number = row_number * col_number
        print(f"{row_number * col_number:5}", end =" ")
    print()
    