'''
Scientists measure an object’s mass in kilograms and its weight in newtons. If you know
the amount of mass of an object in kilograms, you can calculate its weight in newtons with
the following formula:
                        weight = mass X 9.8
Write a program that asks the user to enter an object’s mass, and then calculates its weight.
If the object weighs more than 500 newtons, display a message indicating that it is too
heavy. If the object weighs less than 100 newtons, display a message indicating that it is
too light.
'''
# Getting the mass
CONSTANT = 9.8
mass = eval(input("Enter the mass of an object: "))

# calculations
weight = mass * CONSTANT

if( weight <100 or weight > 500):
    
    check_weight = True

    if check_weight:
        if(weight < 100):
            print("It is too light")
        elif( weight > 500):
            print("It is too heavy")
else:
     print("Outside the targeted ranges")
    
