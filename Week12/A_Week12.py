'''
file: week12 assignment
'''
overall_max_life_exp = 0
overall_max_life_country = ""
overall_min_life_exp = 1500
overall_min_life_country = ""

max_life_exp = 0
max_life_country = ""
min_life_exp = 1500
min_life_country = ""
average_life_exp = 1
average_life_country = ""
sum = 0
count = 0
country_list = []
country_count = 0
with open("life-expectancy.csv") as country_file:
    next(country_file)
    for list in country_file:
        clean_list = list.strip()
        line_list = clean_list.split(",")
        entity = line_list[0].strip()
        if entity not in country_list:
            country_list.append(entity)

    for country in country_list:
        country_count+=1
        print(f"{country_count}:{country}")


# print("1. Afghanistan\n2. Africa\n3. Albania\n4. Algeria\n5. American Samoa\n6. Americas\n7. Andorra\n8. Andorra\n9. Angola\n10. Anguilla")
# print("11. ")
# country_search = int(input("Which country you want to take a look? "))

year_interest = int(input("Enter the year of interest: "))

with open("life-expectancy.csv") as dataset:
    next(dataset)
    for line in dataset:
        clean_line = line.strip()
        line_list = clean_line.split(",")
        entity = line_list[0].strip()
        code = line_list[1].strip()
        year = int(line_list[2])
        life_exp = float(line_list[3])
        if life_exp > overall_max_life_exp:
            overall_max_life_exp = life_exp
            overall_max_life_country = entity
        if life_exp < overall_min_life_exp:
            overall_min_life_exp = life_exp
            overall_min_life_country = entity
        if year_interest == year:
            if life_exp > max_life_exp:
                max_life_exp = life_exp
                max_life_country = entity
            if life_exp < min_life_exp:
                min_life_exp = life_exp
                min_life_country = entity
    sum = sum + life_exp
    count+=1
    average_life_exp = sum/count 
print("For overall: ")
print(f"The overall max life expectancy is: {overall_max_life_exp} from {overall_max_life_country} in {year}")
print(f"The overall min life expectancy is: {overall_min_life_exp} from {overall_min_life_country} in {year}")
print(f"For the {year_interest}: ")
print(f"The average life expectancy across all countries was {average_life_exp}")
print(f"The overall max life expectancy is: {max_life_exp} from {max_life_country} in {year_interest}")        
print(f"The overall min life expectancy is: {min_life_exp} from {min_life_country} in {year_interest}")

            


    # print(line_list)