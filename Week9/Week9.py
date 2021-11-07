'''
file: Week 9 inclass & team activity
Topic: list
'''
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