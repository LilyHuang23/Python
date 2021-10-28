print("Welcome to Chinali Restaurant!")
print("Please answer these questions: ")
pri_chi = float(input("How much is a child's meal? "))
pri_adu = float(input("How much is an adult's meal? "))
num_chi = int(input("How many children are there? "))
num_adu = int(input("How many adults are there? "))
tax_rate  = float(input("What is the sales tax rate? "))
subtotal = pri_chi*num_chi+pri_adu*num_adu
sales_tax = subtotal*tax_rate/100 
total = subtotal + sales_tax 
print(f"Subtotal: ${round(subtotal, 2)}")
print(f"Sales Tax: ${round(sales_tax, 2)}")
print(f"Total: ${round(total, 2)}")

pay_amount = float(input("What is the payment amount? "))
change = pay_amount-total
print(f"Change: ${round(change, 2)}")
print()
print("\U0001F60D Thank you for purchases in Chinali Restaurant. \U0001F60D ")

print("Have a good day! \U0001F917")
print()
import datetime
x = datetime.datetime.now()
print(x)