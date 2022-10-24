'''
Write a program that converts Celsius temperatures to Fahrenheit temperatures. The formula
is as follows:
F =(9/5)*C + 32
The program should ask the user to enter a temperature in Celsius, and then display the
temperature converted to Fahrenheit.
'''

# Getting temperature reading
celcius_temperature = eval(input("Enter the temperature in Celcius:"))

# Computing the Celcius to Fahrenheit
fahrenheit = (9/5) * celcius_temperature + 32

print("The Fahrenheit temperature is",format(fahrenheit,'.2f'))
