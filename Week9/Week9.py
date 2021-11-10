'''
file: Week 9 inclass & team activity
Topic: list

#pre class
#variable = [] == variable = list()
clients = []
clients.append("Lily")
clients.append("Andy")
clients.append("Chloe")

print(clients)

clients.append("Lily")
clients.append("Andy")
clients.append("Chloe")

for clients in clients:
    print(clients)

clients = []
clients_name = ""
while clients_name != "quit":
    clients_name = input("What is the client's name? ")  
    clients.append(clients_name)

for clients_name in clients:
    print(clients_name)

#list of numbers
name = ["Lily", "Apple", "Vivi"]
tips= [9.3, 5.23, 7.58]

running_total = 0

for tip_amount in tips:
    running_total = running_total + tip_amount
    #running_total += tip_amount(line37&38 are the same result)
print(f"The total is: {running_total:.2f}")

#inclass
# A list is a COLLECTION!
# Creating a list variable -> good_name = [ ]
# create an empty list to hold ages
ages = []
# create a list of names
name =[lily, andy, chloe]
# add an age to the age list and a name to the name list
ages.append(12)
print('name: ', name, '\nages', ages)
ages.append(12)
ages.append(12)
ages.append(12)
ages.append(12)
ages.extend([23,33,21,12])
print('name: ', name, '\nages', ages)


remember that for loops are good at going through collections
for item in collection:
    #do something each time we get an item

# use a for loop to go through the lists and print each item
for age in ages:
    print(age)


we can access each item in the list through an index
lists are stored in memory in adjacent memory buckets
                         __________________________
     ages -------------> | 10 | 12 | 23 | 34 | 17 | 
                         --------------------------
                            0    1    2    3    4     index   

# print just the second item in each list
print(ages[1])
print(name[1])
# use a for loop to go through the ages list and
# add all the ages together for a total of all ages
'''
#team activty

print("Enter a list of numbers, type 0 when finished.")
number_list = []
number = ""
while number != 0:
    number = int(input("Enter a number: "))
    number_list.append(number)
count = sum(number_list) 
print("Sum: ", count)
avg = count/len(number_list)
print("Average: ", avg)
print("The smallest positive number is: ",(min([number for number in number_list if number > 0])))
print("The largest number: ",max(number_list))
number_list.sort()
print("The sorted list is: ",number_list)

#comprehension
