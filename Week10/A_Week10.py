'''

'''
print("Enter a list of numbers, type 'end' when finished.")

item_list =[]
item = ""
price_item =[]

while item != "end":
    item = str(input("What item would you like to add?\n"))
    price_item = float(input("What is the price of 'socks'?\n"))
    item_list.append(item)

print(f"{item} has been added to the cart.")
