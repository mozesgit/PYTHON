'''
Write a program that calculates the total amount of a meal purchased at a restaurant. The
program should ask the user to enter the charge for the food, and then calculate the amount
of a 18 percent tip and 7 percent sales tax. Display each of these amounts and the total.
'''
TIP_PERCENTAGE = 0.18
SALES_TAX_PERCENTAGE = 0.07
food_charge = eval(input("Enter the charge for the food:"))
tip_amount = TIP_PERCENTAGE * food_charge
sales_tax_amount = SALES_TAX_PERCENTAGE * food_charge
total = tip_amount + sales_tax_amount + food_charge

print("The tip amount: ",format( tip_amount,'.2f'))
print("The sales tax amount",format( sales_tax_amount,'.2f'))
print("The tip amount",format( total,'.2f'))