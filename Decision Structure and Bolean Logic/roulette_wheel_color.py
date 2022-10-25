'''
On a roulette wheel, the pockets are numbered from 0 to 36. The colors of the pockets are
as follows:
• Pocket 0 is green.
• For pockets 1 through 10, the odd-numbered pockets are red and the even-numbered
pockets are black.
• For pockets 11 through 18, the odd-numbered pockets are black and the even-numbered
pockets are red.
• For pockets 19 through 28, the odd-numbered pockets are red and the even-numbered
pockets are black.
• For pockets 29 through 36, the odd-numbered pockets are black and the even-numbered
pockets are red.
Write a program that asks the user to enter a pocket number and displays whether the
pocket is green, red, or black. The program should display an error message if the user
enters a number that is outside the range of 0 through 36.
'''
# Getting the number 
pocket_number = int(input("Enter the pocket number: "))

# Input Validation
if(pocket_number >= 0 and pocket_number <= 36):
    check_number =True

    if (check_number):
        if(pocket_number == 0):
            print("The pocket is green")
        elif(pocket_number >= 1 and pocket_number <= 10):
            if(pocket_number % 2 == 1):
                print("The pockets are red")
            else:
                print("The pockets are black")
        elif(pocket_number >= 11 and pocket_number <= 18):
            if(pocket_number % 2 == 1):
                print("The pockets are black")
            else:
                print("The pockets are red")
        elif(pocket_number >= 19 and pocket_number <= 28):
            if(pocket_number % 2 == 1):
                print("The pockets are red")
            else:
                print("The pockets are black")
        else:
            if(pocket_number % 2 == 1):
                print("The pockets are black")
            else:
                print("The pockets are red")

else:
    print("The number is out of range")
