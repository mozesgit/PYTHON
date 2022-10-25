'''
The colors red, blue, and yellow are known as the primary colors because they cannot
be made by mixing other colors. When you mix two primary colors, you get a secondary
color, as shown here:
When you mix red and blue, you get purple.
When you mix red and yellow, you get orange.
When you mix blue and yellow, you get green.
Design a program that prompts the user to enter the names of two primary colors to mix. If
the user enters anything other than “red,” “blue,” or “yellow,” the program should display
an error message. Otherwise, the program should display the name of the secondary color
that results.
'''
first_color = input("Enter the first primary color: ")
second_color = input("Enter the second primary color: ")
color = (first_color == "red" or first_color == "blue" or first_color == "yellow") and \
    (second_color == "red" or second_color == "blue" or second_color == "yellow")
if(color):
    color_check = True

    if color_check:
        if(first_color == "red" and second_color == "blue"):
            print("The second color is purple")
        elif(first_color == "red" and second_color == "yellow"):
            print("The second color is Orange")
        else:
            print("The second color is green")
else:
    print("Not red,blue or yellow")
