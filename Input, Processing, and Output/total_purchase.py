'''
A customer in a store is purchasing five items. Write a program that asks for the price of
each item, and then displays the subtotal of the sale, the amount of sales tax, and the total.
Assume the sales tax is 7 percent
'''
SALES_TAX = 0.07

# Getting the price of each item
item1_price = eval(input("Enter the price for first item: "))
item2_price = int(input("Enter the price for second item: "))
item3_price = int(input("Enter the price for third item: "))
item4_price = int(input("Enter the price for fourth item: "))
item5_price = int(input("Enter the price for fifth item: "))

# Calcu;ations
subtotal = item1_price + item2_price +\
     item3_price + item4_price + item5_price

sales_tax_amount = subtotal * SALES_TAX

total_amount = subtotal + sales_tax_amount

# Output
print("Subtotal of the sale:", format(subtotal,',.2f'))
print("The amount of sales tax:", format(sales_tax_amount,',.2f') )
print("The total amount:", format(total_amount,'.2f'))