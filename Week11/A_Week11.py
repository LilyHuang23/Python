'''
file: week11 prove milestone
'''

with open("life-expectancy.csv") as dataset:
    next(dataset)
    # year = int(input("Enter the year of interest: "))
    for line in dataset:
        clean_line = line.strip()
        line_list = clean_line.split(" ")
        # entity = line_list[0]
        # code = line_list[1]
        # year = line_list[2]
        # life_exp = line_list[3]
        print(line_list)