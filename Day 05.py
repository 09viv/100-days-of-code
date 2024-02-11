# Random password generator
import random

print("Welcome to the password generator..")

letter = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n,'
          'o','p','q','r','s','t','u','v','w','x','y','z'
          'A','B','C','D','E','F','G','H','I','J','K','L','M',
          'N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

numbers = ['0','1','2','3','4','5','6','7','8','9']

symbol = ['!','@','#','$','%','&','*']

new_letter = int(input("Enter number of letters you wish in your password: "))
new_numbers = int(input("Enter number of numbers you wish in your password: "))
new_symbol = int(input("Enter number of symbol you wish in your password: "))


pass_list = []
for char in range (1,new_letter + 1):
    pass_list += random.choice(letter)

for char in range (1, new_numbers + 1):
    pass_list += random.choice(numbers)

for char in range (1, new_symbol + 1):
    pass_list += random.choice(symbol)


random.shuffle(pass_list)

password = ""
for char in pass_list:
    password += char
print(f"Your password is {password}")
 