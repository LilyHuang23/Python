'''
w4 inclass
'''

from abc import get_cache_token
import math
'''

#f-strings(new vs old)
a = 100
b = 45
print(f'this is stringwith formatting...{5*23 - 12:.2f}{b}{"nice":>10}')#new
print('this is stringwith formatting...{:>.2f}{b} {} {:>10}'.format((5*23-12),b,"nice"))#old


# formatting reference sheet
print(f'here\'s another example: {a:*^10.2f} and {b:#^20}')

#calculate f = ma (force = mass * acceleration)
mass = float(input("mass(kg): "))
accel = float (input('acceleration(m/s^2): '))

force = mass * accel
print(force)

#print result formatted nicely and with 4 decimals
print(f'force is {force: .4f}')


#what do  I do there is a function in the math 
#that i need to use?
x = math.sin(75)
print(f'{x:.2f}')
'''
# team activty
print("Welcome to the velocity calculator. Please enter the following: ")
m = float(input("Mass (in kg): "))
g = float(input("Gravity (in m/s^2, 9.8 for Earth, 24 for Jupiter): "))
t = float(input("Time (in seconds): "))
p = float(input("Density of the fluid (in kg/m^3, 1.3 for air, 1000 for water): "))
A = float(input("Cross sectional area (in m^2): "))
C = float(input("Drag constant (0.5 for sphere, 1.1 for cylinder): "))

c = (1 / 2) * p * A * C
v = math.sqrt(m*g/c) * (1 - math.exp((-math.sqrt(m*g*c)/m)*t))
print(f"The inner value of c is: {c:.3f}")
print(f"The velocity after {t} seconds is: {v:.3f} m/s")

# stretch challenge
# skydiver
m = 70
A = 0.18
C = 0.7
p = 1.21
c = (1 / 2) * p * A * C
v = math.sqrt(m*g/c) * (1 - math.exp((-math.sqrt(m*g*c)/m)*t))
print(f"The termial velocity is {v:.2f}")
#Jupiter
