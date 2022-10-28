'''
A bug collector collects bugs every day for five days. Write a program that keeps a running
total of the number of bugs collected during the five days. The loop should ask for the
number of bugs collected for each day, and when the loop is finished, the program should
display the total number of bugs collected.
'''
# Analysis:
# maximum number of days
MAX_DAYS = 5

# accumulator variable
running_total = 0

# # counter
# counter = 0
# while counter < MAX_DAYS:
#     # Getting number of bugs
#     number_of_bugs = int(input("Enter the number of bugs collected per day: "))

#     # Accumulating the number of bugs
#     running_total += number_of_bugs

#     # Updating counter
#     counter += 1
# # Output
# print(f"The the total number of bugs after {MAX_DAYS} days is {running_total}")

# OR
for _ in range(MAX_DAYS):

    # Getting the number of collected bugs
    number_of_bugs = int(input("Enter the number of bugs collected per day:"))

    # Accumulating the number of bugs
    running_total += number_of_bugs

# Output
print(f"The total number of bugs collected after {MAX_DAYS} days is {running_total}")
