
values_list = []

def average(values_list):
    sum = 0
    for item in values_list:
        sum += item
    
    # calculating the average
    avg = sum / len(values_list)

    return avg

# Reading the values
values_total = int(input("Enter the total number of values:"))
for i in range(values_total):
    value = float(input("Enter the value:"))
    values_list.append(value)

mean = average(values_list)

print(f"The average is {mean}")