'''
Write a program that will ask the user to enter the amount of a purchase. The program
should then compute the state and county sales tax. Assume the state sales tax is 5 percent
and the county sales tax is 2.5 percent. The program should display the amount of the purchase,
the state sales tax, the county sales tax, the total sales tax, and the total of the sale
(which is the sum of the amount of purchase plus the total sales tax).
Hint: Use the value 0.025 to represent 2.5 percent, and 0.05 to represent 5 percent.
'''
STATE_TAX_PERCENTAGE = 0.05 # 5% 
COUNTRY_TAX_PERCENTAGE = 0.025 # 2.5%
# Getting the amount of a purchase
purchase_amount = eval(input("Enter the amount of purchase:"))

state_tax = purchase_amount * STATE_TAX_PERCENTAGE
country_tax = purchase_amount * COUNTRY_TAX_PERCENTAGE
total_tax = state_tax + country_tax
total_sale = purchase_amount + total_tax
print(f'''
    The amount of the purchase: {purchase_amount}
    The amount of state tax: {state_tax}
    The amount of country tax: {country_tax}
    The total sales: {total_tax}
    The total of the sale: {total_sale}
''')
