'''
One acre of land is equivalent to 43,560 square feet. Write a program that asks the user to
enter the total square feet in a tract of land and calculates the number of acres in the tract.
Hint: Divide the amount entered by 43,560 to get the number of acres.
'''
ONE_ACRE_IN_SQUARE_FEET = 43560

# Getting the square feet of the land
total_square_feet = eval(input("Enter the total square feet of land:"))

# calculating the number of acres

acres = total_square_feet / ONE_ACRE_IN_SQUARE_FEET

print("The total number of acres will be ", format(acres,'.2f'),"acres")

