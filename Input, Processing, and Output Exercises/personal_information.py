'''
Write a program that displays the following information:
• Your name
• Your address, with city, state, and ZIP
• Your telephone number
• Your college major
'''
name = input("Enter your name:")
address = input("Enter your address:")
city = input("Enter the name of the city:")
state = input("Name of the state:")
zip = input("Enter the zip code:")

print(f''' 
    Name:{name}
    Address:{address}
    City:{city}
    State:{state}
    Zip:{zip}
''')