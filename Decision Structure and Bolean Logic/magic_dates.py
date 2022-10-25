'''
The date June 10, 1960, is special because when it is written in the following format, the
month times the day equals the year:
6/10/60
Design a program that asks the user to enter a month (in numeric form), a day, and a twodigit
year. The program should then determine whether the month times the day equals the
year. If so, it should display a message saying the date is magic. Otherwise, it should display
a message saying the date is not magic.
'''
# Getting inputs from the user
month = int(input("Enter the month: "))
day = int(input("Enter the day: "))
twodigit_year =int(input("Enter the year in two digits: "))

if(month * day == twodigit_year):
    print("The date is magic")
else:
    print("The day is not magic")
