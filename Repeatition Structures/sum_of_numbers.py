'''
Write a program with a loop that asks the user to enter a series of positive numbers. The
user should enter a negative number to signal the end of the series. After all the positive
numbers have been entered, the program should display their sum.
'''
sum = 0

number = eval(input("Enter the positive number:"))

while True:

    sum += number

    number = eval(input("Enter the positive number:"))

    if( number < 0):
        break
    else:
        continue
print(f"The sum of numbers is {sum}")

    
