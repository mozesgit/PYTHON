'''
Write a program that calculates the amount of money a person would earn over a period
of time if his or her salary is one penny the first day, two pennies the second day, and
continues to double each day. The program should ask the user for the number of days.
Display a table showing what the salary was for each day, and then show the total pay at
the end of the period. The output should be displayed in a dollar amount, not the number
of pennies.
'''
# Accumulator Variable
running_total = 0
# Getting the number of days
num_days = int(input("Enter the number of days: "))
print("Day            Dollars")
for  day in range(num_days):
    
    dollar = 0.01 * (2) ** day

    # Accumulating the total
    running_total += dollar

    print(f"{day + 1}" + "\t\t" + format(dollar,'.2f'))

print("Total:        ", format(running_total,'.2f'))