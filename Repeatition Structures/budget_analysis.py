'''
Write a program that asks the user to enter the amount that he or she has budgeted for
a month. A loop should then prompt the user to enter each of his or her expenses for the
month and keep a running total. When the loop finishes, the program should display the
amount that the user is over or under budget.
The Bug Collector
'''
# Analysis:

# accumulator variable
running_total = 0

# Getting the budgeted amount
budget_amount = eval(input("Enter the budgeted amount for a month:"))

# Getting expenses
while True:
    expense = eval(input("Enter the expense amount:"))
    # Accumulating the expenses
    running_total += expense

    # Asking the user if he or she wants to continue
    choice = input("do you want to continue or not?[y|n][confirm]:")

    if(choice == 'y'):
        continue
    else:
        break

# Checking the amount
if(running_total > budget_amount):
    print("The total amount of expenses:", format(expense,',.2f'), "is over", format(budget_amount,',.2f'))
else:
    print("The total amount of expenses:", format(expense,',.2f'),"is under", format(budget_amount,',.2f'))