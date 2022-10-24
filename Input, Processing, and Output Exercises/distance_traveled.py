'''
Assuming there are no accidents or delays, the distance that a car travels down the interstate
can be calculated with the following formula:
Distance = Speed x Time

A car is traveling at 70 miles per hour. Write a program that displays the following:
• The distance the car will travel in 6 hours
• The distance the car will travel in 10 hours
• The distance the car will travel in 15 hours
'''


speed = 70
first_interval = 6
second_interval = 10
third_interval = 15

# Calculating the distance for each time of travel
distance1 = speed * first_interval
distance2 = speed * second_interval
distance3 = speed * third_interval

# Displaying the traveled distance
print(f'''
    The distance travelled in 6 hours : {distance1} miles
    The distance travelled in 10 hours : {distance2} miles
    The distance travelled in 15 hours : {distance3} miles

''')