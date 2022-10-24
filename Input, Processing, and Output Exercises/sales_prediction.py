'''
A company has determined that its annual profit is typically 23 percent of total sales. Write
a program that asks the user to enter the projected amount of total sales, and then displays
the profit that will be made from that amount.
Hint: Use the value 0.23 to represent 23 percent
'''

# Getting the projected amount
projected_amount = eval(input("Enter the amount after total sales:"))

# calculating annual profit from total sales
annual_profit = projected_amount * 0.23


print("The annual profit will be", format(annual_profit, '.2f'))