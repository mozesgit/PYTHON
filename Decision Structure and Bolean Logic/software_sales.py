'''
A software company sells a package that retails for $99. Quantity discounts are given
according to the following table:
Quantity Discount
10–19 10%
20–49 20%
50–99 30%
100 or more 40%
Write a program that asks the user to enter the number of packages purchased. The program
should then display the amount of the discount (if any) and the total amount of the
purchase after the discount.
'''
package_charge = 99

# Getting the number of packages
num_packages = int(input("Enter the number of packages: "))
if(not(package_charge < 10)):
    if(num_packages >= 10 and num_packages <= 19):
        discount_amount = 0.1 * num_packages
        total_amount = package_charge - discount_amount
    
        print("The discount amount: $" + format(discount_amount,'.2f'))
        print("The total amount: $" + format(total_amount,'.2f'))

    elif(num_packages > 19 and num_packages <= 49):
        discount_amount = 0.2 * num_packages
        total_amount = package_charge - discount_amount

        print("The discount amount: $" + format(discount_amount,'.2f'))
        print("The total amount: $" + format(total_amount,'.2f'))

    elif(num_packages > 49 and num_packages <= 99):
        discount_amount = 0.3 * num_packages
        total_amount = package_charge - discount_amount
        
        print("The discount amount: $" + format(discount_amount,'.2f'))
        print("The total amount: $" + format(total_amount,'.2f'))

    else:
        discount_amount = 0.4 * num_packages
        total_amount = package_charge - discount_amount
        
        print("The discount amount: $" + format(discount_amount,'.2f'))
        print("The total amount: $" + format(total_amount,'.2f'))
else:
    print("The package number needs to be atleast 10 to get the discount")