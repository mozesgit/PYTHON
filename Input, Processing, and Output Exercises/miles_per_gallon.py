'''
A car’s miles-per-gallon (MPG) can be calculated with the following formula:
        MPG = Miles driven Gallons of gas used
Write a program that asks the user for the number of miles driven and the gallons of gas
used. It should calculate the car’s MPG and display the result
'''
# Getting the miles driven and gallons of gas used
miles_driven = eval(input("Enter the miles driven: "))
gas_gallons = eval(input("Enter the number of gas gallons: "))

cars_mpg = miles_driven * gas_gallons
print(f"The car's MPG: {cars_mpg} mpg")