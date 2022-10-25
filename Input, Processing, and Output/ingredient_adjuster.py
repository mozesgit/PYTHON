'''
A cookie recipe calls for the following ingredients:
• 1.5 cups of sugar
• 1 cup of butter
• 2.75 cups of flour
The recipe produces 48 cookies with this amount of the ingredients. Write a program that
asks the user how many cookies he or she wants to make, and then displays the number of
cups of each ingredient needed for the specified number of cookies.
'''

# Getting the number of cookies
cookies_number = int(input("Enter the number of cookies:"))

# calculations
sugar_adjustment = (1.5/48) * cookies_number
butter_adjustment = (1/48) * cookies_number
flour_adjustment = (2.75/48) * cookies_number


print("cups of sugar will be: " + format(sugar_adjustment,'.2f')  + " cups")
print("cups of butter will be: " + format(butter_adjustment,'.2f')  + " cups")
print("cups of flour wil be: " + format(flour_adjustment,'.2f')  + " cups")
