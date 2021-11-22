'''
File: Week 10 in class & Team activity
Topic: Index


nums = []
nums = [1,3,5,7]
print(f"The thrid number is: {nums[2]}")#using the index

length = len(nums)
print(length)

#loop through 
for item in nums:
    print(item)
#loop through a list using index(and range)
print("\nprint with index")
for index in range(len(nums)):
    print(nums[index])
    #print(f"{index=} {nums[index]=}")

#user friendly
for index in range(len(nums)):
    #print(nums[index])
    print(f"{index+1}... {nums[index]}")
#index for two list
names=["lily","andy","chloe"]
ages = [10,23,25]
for index in range(len(names)):
    #print(nums[index])
    print(f"{index+1}... {names[index]}, age:{ages[index]}")

#input the variable
print("\nbefore change 2nd item(index1):",ages)
ages[1] = 19

print("after change:",ages)
# ask the user which item they want to replace
# if I used user friendly numbers to display, 
# I need to -1 to get the correct index 
for i in range(len(ages)):
    print(i+1, ages[1])
index = int(input("which age do you want to change:"))

# show the list again to show the new age is in the list
# print('\naltered list:', ages)



# remove an item from the nums list with pop()
nums = [1,5,7,9]  # initialized list
print('\nbefore popping from nums')
print(nums)
popped_item = nums.pop(1)#index number
print("\nafter popping from nums")
print(nums)
# print('\nafter popping from nums')

# print the item removed (popped)
print(popped_item)
'''
#team
print("Enter the names and balances of bank accounts (type: quit when done)")
name_list = []
num_list = []

name = ""
num = ""

while name !="end":
    name = str(input("What is the name of this account?" ))
    if name !="end":
        name_list.append(name)
        num = float(input("What is the balance? $"))
        num_list.append(num)

print("Account Information: ")
for i in range(len(name_list)):
    print(f"{i+1},{name_list[i]},{num_list[i]}")


Total = sum(num_list)
print(f"Total: ${Total}")

Average = Total/len(num_list)
print(f"Average: ${Average}")

highest = max(num_list)
print(f"The highest balance: ${highest}")


change = str(input("Do you want to update an account? yes/no\n"))

change = ""

while change =="yes":
    update = float(input("What account index do you want to update? "))
    new_num = float(input("What is the new amount? \n$ "))
else:
    print("Sweet!")







# print()

# BONUS: insert a value at index 1 (may confuse some)
# val = (input('Enter a value to insert at index 1: '))
# nums.insert(1, val)
# print('list with value inserted at index 1: ', nums)
# print()


