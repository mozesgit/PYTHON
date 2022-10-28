'''
Write a program that displays a table of the Celsius temperatures 0 through 20 and
their Fahrenheit equivalents. The formula for converting a temperature from Celsius to
Fahrenheit is
F = (9/5)*C + 32
where F is the Fahrenheit temperature and C is the Celsius temperature. Your program must
use a loop to display the table.
'''

print("Celcius      Fahrenheit")
print("=======================")
for celcius in range(20):
    
    # Converting celcius to fahrenheit
    fahrenheit = (9 / 5) * celcius + 32

    print("|" + str(celcius) + "\t" + "|" + "\t" + format(fahrenheit,'.1f') + "|")
    print("---------------------")