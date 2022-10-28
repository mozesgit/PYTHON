'''
Write a program that uses nested loops to collect data and calculate the average rainfall
over a period of years. The program should first ask for the number of years. The outer loop
will iterate once for each year. The inner loop will iterate twelve times, once for each month.
Each iteration of the inner loop will ask the user for the inches of rainfall for that month.
After all iterations, the program should display the number of months, the total inches of
rainfall, and the average rainfall per month for the entire period.
'''
# Accumulator variables
running_total_inches = 0
num_months = 0

# Getting the number of years
num_years = int(input("Enter the number of years:"))

for year in range(num_years):
    print(f"Year {year + 1}")
    print()
    for month in range(12):
        # Getting rainfall measurements in inches
        print(f"Rainfall inches for month {month + 1}")
        rainfall_inches = eval(input("Enter rainfall inches:"))

        # accumulating the number of inches
        running_total_inches += rainfall_inches
        num_months += 1

print()
# Calculating the average
average = running_total_inches / num_months

print(f"The number of months: {num_months}")
print("The total inches of rainfall:",format(running_total_inches,'.1f'))
print("The average(rainfall/month):",format(average,'.1f'))
print()