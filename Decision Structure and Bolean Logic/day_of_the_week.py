'''
Write a program that asks the user for a number in the range of 1 through 7. The program
should display the corresponding day of the week, where 1 = Monday, 2 = Tuesday,
3 = Wednesday, 4 = Thursday, 5 = Friday, 6 = Saturday, and 7 = Sunday. The program should
display an error message if the user enters a number that is outside the range of 1 through 7
'''

# Getting the number
number = int(input("Enter the number in the range of 1-7:"))
# validating
if( number >= 1 and number <= 7):

    # Diplaying the output
    if(number == 1):
        print("Monday")
    elif(number == 2):
        print("Tuesday")
    elif(number == 3):
        print("Wednesday")
    elif(number == 4):
        print("Thursday")
    elif(number == 5):
        print("Friday")
    elif(number == 6):
        print("Sartuday")
    else:
        print("Sunday")
        
else:
    print("Out of range")
