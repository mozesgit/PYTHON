'''
The area of a rectangle is the rectangle’s length times its width. Write a program that asks
for the length and width of two rectangles. The program should tell the user which rectangle
has the greater area, or if the areas are the same
'''
# Getting dimensions from first rectangle
length1 = eval(input("Enter the length for the first rectangle: "))
width1 = eval(input("Enter the width for the first rectangle:"))

# Getting dimensions from second rectangle
length2 = eval(input("Enter the length for second rectangle: "))
width2 = eval(input("Enter the width for the second rectangle:"))

# computations
area1 = length1 * width1
area2 = length2 * width2

if( area1 == area2):
    print(f"The area {area1} is the same for two rectangles")
else:
    if(area1 >= area2):
        print(f"The area {area1} for the first rectangle is greater")
    else:
        print(f"The area {area2} for the second rectangle is greater")