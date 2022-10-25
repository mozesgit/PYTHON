'''
Write a program that asks the user for the number of males and the number of females registered
in a class. The program should display the percentage of males and females in the class.
'''
# Getting the number of males and females

num_males = int(input("Enter the number of males: "))
num_females = int(input("Enter the number of females: "))

total = num_males + num_females

male_percentage = (num_males/total)  # this will be in decimal point
female_percentage = (num_females/total) # this will be in decimal point

print("The male percentage: ", str(male_percentage) , \
     "which is the same as ", str(male_percentage * 100) + "%")
    
print("The female percentage: ", str(female_percentage) , \
     "which is the same as ", str(female_percentage * 100) + "%")
