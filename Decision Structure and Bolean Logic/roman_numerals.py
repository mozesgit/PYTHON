'''
Write a program that prompts the user to enter a number within the range of 1 through 10.
The program should display the Roman numeral version of that number. If the number is
outside the range of 1 through 10, the program should display an error message.
'''

# Getting the numbers
number = int(input("Enter the number in the range of 1-10: "))

# if(number >= 1 and number <= 10):
    # if(number == 1):
    #     print("Roman numeral: I")
    # else:
    #     if(number == 2):
    #         print("Roman numeral: II")
    #     else:
    #         if(number == 3):
    #             print("Roman numeral: III")
    #         else:
    #             if(number == 4):
    #                 print("Roman numeral: IV")
    #             else:
    #                 if(number == 5):
    #                     print("Roman numeral:V")
    #                 else:
    #                     if(number == 6):
    #                         print("Roman numeral:VI")
    #                     else:
    #                         if(number == 7):
    #                             print("Roman numeral:VII")
    #                         else:
    #                             if(number == 8):
    #                                 print("Roman numeral:VIII")
    #                             else:
    #                                 if(number == 9):
    #                                     print("Roman numeral: IX")
    #                                 else:
    #                                     print("Roman numeral: X")

# else:
    # print("The number is out of range")

# OR 
if(number >= 1 and number <= 10):
    if(number == 1):
        print("Roman numeral: I")
    elif(number == 2):
        print("Roman numeral: II")
    elif(number == 3):
        print("Roman numeral: III")
    elif(number == 4):
        print("Roman numeral: IV")
    elif(number == 5):
        print("Roman numeral:V")
    elif(number == 6):
        print("Roman numeral: VI")
    elif(number == 7):
        print("Roman numeral: VII")
    elif(number == 8):
        print("Roman numeral: VIII")
    elif(number == 9):
        print("Roman numeral: IX")
    else:
        print("Roman numeral: X")
else:
    print("The number is out of range")