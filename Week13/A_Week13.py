'''
file: Wind Chill Calculations
'''
#function to calculate wind chill
def wind_calculation(temp, wind_speed):
    wind_chill = 35.74 + 0.6215*temp - 35.75*(wind_speed ** .16) + 0.4275*temp*(wind_speed ** .16)
    return wind_chill
#function to convert c to f
def temp_convert(c):
        convert_f = (c * 1.8) + 32 
        return convert_f
#if temp is in c, convert (call function to convert f)
#loop to go through wind spped 5-60 in increments of 5
#print info
#35.74 + 0.6215T - 35.75(V0.16) + 0.4275T(V0.16)
#ask user for temp
temp = int(input("What is the temperature?\n"))
unite = input("Fahrenheit or Celsius (F/C)?")
if unite == "c":
    temp = temp_convert(temp)
#Celsius or Fahrenheit
for speed in range(5, 61, 5):
    #call wind chill function
    print(f"At temperature {temp}{unite}, and wind speed {speed}, the windchill is: {wind_calculation(temp, speed)}")

    #print the info
