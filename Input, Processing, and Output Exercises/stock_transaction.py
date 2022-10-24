'''
    Last month Joe purchased some stock in Acme Software, Inc. Here are the details of the
purchase:
• The number of shares that Joe purchased was 2,000.
• When Joe purchased the stock, he paid $40.00 per share.
• Joe paid his stockbroker a commission that amounted to 3 percent of the amount he
paid for the stock.
Two weeks later Joe sold the stock. Here are the details of the sale:
• The number of shares that Joe sold was 2,000.
• He sold the stock for $42.75 per share.
• He paid his stockbroker another commission that amounted to 3 percent of the amount
he received for the stock.
Write a program that displays the following information:
• The amount of money Joe paid for the stock.
• The amount of commission Joe paid his broker when he bought the stock.
• The amount that Joe sold the stock for.
• The amount of commission Joe paid his broker when he sold the stock.
• Display the amount of money that Joe had left when he sold the stock and paid his
broker (both times). If this amount is positive, then Joe made a profit. If the amount is
negative, then Joe lost money.
'''
NUMBER_OF_SHARES = 2000
SHARE_CHARGE = 40
FIRST_COMMISSION_PERCENTAGE = 0.03
SHARE_PRICE = 42.75
SECOND_COMMISSION_PERCENTAGE = 0.03

# Calculations
amount_paid = SHARE_CHARGE * NUMBER_OF_SHARES
first_commission_pay = amount_paid * 0.03
sells_amount = SHARE_PRICE * NUMBER_OF_SHARES
second_commission_pay = sells_amount * 0.03
amount_left = sells_amount -(first_commission_pay + second_commission_pay)
print("The amount of money Joe paid: $" + format(amount_paid,',.2f'))
print("The commission paid when he bought the stock: $" +format(first_commission_pay,',.2f'))
print("The total amount after selling the stock: $" + format(sells_amount,',.2f'))
print("The commission paid after selling the stock: $" + format(second_commission_pay,',.2f'))
print("The amount left: $" + format(amount_left,',.2f'))
