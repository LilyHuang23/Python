'''
File: W10 Assignment
'''
# print("Enter a list of numbers, type 'end' when finished.")

item_list =[]
item = ""
price = ""
price_item =[]
# price_item = float(input("What is the price of 'socks'?\n"))
#         price_item.append(price)
#         item_list.append(item)
 
print("Welcome to the Shopping Cart Program! ")

action = "" 

while action != "5":
    print("Please input one of the following: ")
    print("1. Add item\n2. View cart\n3. Remove item\n4. Compute total\n5. Quit")
    action = input("Please enter an action: ")
    if action == "1":
        item = str(input("What item would you like to add?\n"))
        price= float(input(f"What is the price of {item}?\n"))
        price_item.append(price)
        item_list.append(item) 
        print(f"{item} has been added to the cart.")
    elif action == "2":
        print("The contents of the shopping cart are: ")
        for i in range(len(item_list)):
            print(f"{i+1}.{item_list[i]} - ${price_item[i]:.2f}")
    elif action == "3":
        remove = int(input("Which item number would you like to remove? "))
        item_list.pop(remove-1)
        price_item.pop(remove-1)
        print("Item remove")
    elif action == "4":
        total = sum(price_item)
        print(f"The total price of the items in the shopping cart is ${total:.2f}")
    else:
        print("thank you!")



