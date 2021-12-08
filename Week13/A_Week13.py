'''
file: Wind Chill Calculations
'''
#function to calculate wind chill
def wind_calculation(temp, wind_spped):
    wind_chill = 35.74 + 0.6215*temp - 35.75*(wind_speed ** .16) + 0.4275*temp(wind_spped ** .16)
    return wind_chill
#function to convert c to f
#if temp is in c, convert (call function to convert f)
#loop to go through wind spped 5-60 in increments of 5
#print info
#35.74 + 0.6215T - 35.75(V0.16) + 0.4275T(V0.16)


#ask user for temp
temp = int(input("What is the temperature?\n"))
("Fahrenheit or Celsius (F/C)?"))
#Celsius or Fahrenheit
for speed in range(5, 61, 5):
    #call wind chill function

    #print the info
