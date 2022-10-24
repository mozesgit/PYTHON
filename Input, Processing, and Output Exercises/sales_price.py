
def get_sales(price):

    # Calculating the discount amount
    discount_amount = (price * 20) / 100

    # Finding the final sales price
    new_price = price - discount_amount

    return [original_price,discount_amount,new_price]

# getting the original price
original_price = float(input("Enter the original price:"))
output = get_sales(original_price)

# Displaying the result
for item in range(len(output)):
    if(item == 0):
        print(f"The original price is {output[item]}\n")
    elif(item == 1):
        print(f"The Discount amount is {output[item]}\n")
    elif(item == 2):
        print(f"The new price is {output[item]}\n")

