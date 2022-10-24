'''
A cookie recipe calls for the following ingredients:
• 1.5 cups of sugar
• 1 cup of butter
• 2.75 cups of flour
The recipe produces 48 cookies with this amount of the ingredients. Write a program that
asks the user how many cookies he or she wants to make, and then displays the number of
cups of each ingredient needed for the specified number of cookies.
'''
# 1.5 cups of sugar produces 16 cookies out of 48 cookies
# 1 cup of butter produces 8 cookies out of 48 cookies
# 2.75 cups of flour produces 24 cookies out of 48 cookies 
# Summation of 1.5,1,2.75
TOTAL_RATIO = 6
# Getting the number of cookies
cookies_number = int(input("Enter the number of cookies:"))

# calculations
cups_of_sugar = (16 / cookies_number) * 6
cups_of_butter = (8 / cookies_number) * 6
cups_of_flour = (24 / cookies_number) * 6

print("The cups of sugar:",format(cups_of_sugar,'.1f'))
print("The cups of butter:",format(cups_of_butter,'.1f'))
print("The cups of flour:",format(cups_of_flour,'.1f'))