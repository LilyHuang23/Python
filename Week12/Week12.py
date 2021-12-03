'''
File: Week 12 in class & Team activity
Topic:
'''
'''
# pre-class
max_price = -1
max_product = "" # It doesn't matter what you set this to, it just needs to be declared

shopping_cart = [
    ["Chips", 2.99],
    ["Bread", 2.50],
    ["Milk", 3.19],
    ["Ice Cream", 6.99],
    ["Cheese", 5.99],
    ["Candy bar", 0.99]
]

for item in shopping_cart:
    product_name = item[0] # Product name is the first part
    price = item[1] 

    if price > max_price:
        # This is the new max
        max_price = price

        # Also save this product name as the max product
        max_product = product_name

print(f"The maximum price is: {max_price}")
print(f"The product with the maximum price is: {max_product}")
'''
'''
#inclass-1
# take a look at file.txt
# use best practice to open file.txt
sum = 0
with open("file.txt") as file:
    # if there's a header line, skip it
    #next(file)
    # loop through the lines
    for line in file:
        print(line)
        # strip whitespace and print line
        line = line.strip()
        # split line into parts (a list) and print list
        line_list = line.split(" ")
        print(line_list)
        # save parts in new variables so they're easier to use
        word1 = line_list[0]
        word2 = int(line_list[1])#this is a unmber
        word3 = line_list[2]
        word4 = line_list[3]
        print(f" {word1} {10*word2}")
        sum += word2

#team activity
max = 0
max_chapter = ""
with open("books_and_chapters.txt") as book_file:
    for part in book_file:
        stripped=part.strip()
        part_list = stripped.split(":")
        book = part_list[0].strip()
        scripture = part_list[2].strip()
        chapter = int(part_list[1])
        print(f"Scripture: {scripture}, Book: {book}, Chapters: {chapter}")
        if chapter > max:
            max = chapter
            max_chapter = book 
print(f"The book with the most chapters is: {max_chapter}")
print(f"It has {max} chapters.")
'''
# STRETCH CHALLENGE
max = 0
max_chapter = ""
question = input("which volume of scriptures they would like to learn about?\n")

with open("books_and_chapters.txt") as book_file:
    for part in book_file:
        stripped=part.strip()
        part_list = stripped.split(":")
        book = part_list[0].strip()
        scripture = part_list[2].strip()
        chapter = int(part_list[1])
        if question == "Old Testament":
            if scripture == 'Old Testament':
                print(f"Scripture: {scripture}, Book: {book}, Chapters: {chapter}")  
            if chapter > max:
                max = chapter
                max_chapter = book 
            
        elif question == "New Testament":
            if scripture == 'New Testament':
                print(f"Scripture: {scripture}, Book: {book}, Chapters: {chapter}")    
            if chapter > max:
                max = chapter
                max_chapter = book 
           
        elif question == "Book of Mormon":
            if scripture == 'Book of Mormon':
                print(f"Scripture: {scripture}, Book: {book}, Chapters: {chapter}")           
                if chapter > max:
                    max = chapter
                    max_chapter = book 
           
        elif question == "Doctrine and Covenants":
            if scripture == 'Doctrine and Covenants':
                print(f"Scripture: {scripture}, Book: {book}, Chapters: {chapter}") 
            if chapter > max:
                max = chapter
                max_chapter = book 
        
        elif question == "Pearl of Great Price":
            if scripture == 'Pearl of Great Price':
                print(f"Scripture: {scripture}, Book: {book}, Chapters: {chapter}") 
            if chapter > max:
                max = chapter
                max_chapter = book 
            
        else:
            print("Sorry , the system can't read.")
    print(f"The book with the most chapters is: {max_chapter}")
    print(f"It has {max} chapters.")


        