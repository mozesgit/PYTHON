'''
Running on a particular treadmill you burn 4.2 calories per minute. Write a program that
uses a loop to display the number of calories burned after 10, 15, 20, 25, and 30 minutes.
'''
# Analysis:

# Calorie burn rate
rate = 4.2

# using for loop to display the results
for minutes in [10,15,20,25,30]:
    burned_calories = rate * minutes

    print(f"The number of calories burned after {minutes}",\
         f"minuntes will be {burned_calories} calories")
