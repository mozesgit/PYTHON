'''
Assuming the ocean’s level is currently rising at about 1.6 millimeters per year, create an
application that displays the number of millimeters that the ocean will have risen each year
for the next 25 years.
'''
rate = 1.6
for year in range(25):
    num_milimeters = rate * (year + 1)

    print("Year " + str(year + 1) + " : " + format(num_milimeters,'.2f') +" milimeters")