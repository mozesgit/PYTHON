'''
The Fast Freight Shipping Company charges the following rates:
Weight of Package Rate per Pound
2 pounds or less $1.50
Over 2 pounds but not more than 6 pounds $3.00
Over 6 pounds but not more than 10 pounds $4.00
Over 10 pounds $4.75
Write a program that asks the user to enter the weight of a package and then displays the
shipping charges.
'''
package_weight = eval(input("Enter the package weight: "))

# checking the package weight
if(package_weight <= 2):
    print("Rate per pound is $1.50")
elif(package_weight > 2 and package_weight <= 6):
    print("Rate per pound is $3.00")
elif(package_weight > 6 and package_weight <= 10):
    print("Rate per pound is $4.00")
else:
    print("Rate per pound is $4.75")