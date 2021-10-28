'''
file:team activity
authour:Lily
'''

last_name= input("Last_name: ")
first_name= input("First_name: ")
job_title= input("Job title: ")
num_id= input("ID_number: ")

email_address= input("Eamil address: ")
num_phone= input("Phone humber: ")
hair= input("What is your hair color: ")
eyes= input("What is your eye color: ")
month= input("What month you started: ")
training= input("Have you recive any training: ")
#print out
print("The ID Card is: ")
print("-"*40)
print(f"{last_name.upper()} {first_name.lower()}")
print(job_title.title())
print(f"ID: {num_id}")
print()
print(email_address.lower())
print(num_phone)
print()
print(f"Hair: {hair:20} Eyes: {eyes}")
print(f"Month: {month:19} Training: {training}")

print("-"*40)
