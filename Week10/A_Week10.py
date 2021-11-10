'''

'''
print("Enter a list of numbers, type 'end' when finished.")

item_list =[]
item = ""

while item != "end":
    item = str(input("What item would you like to add?\n"))
    item_list.append(item)
    price_item = float(input("What is the price of 'socks'?\n"))
print(f"{item_add} has been added to the cart.")
