#Day 02 task of 100 days of code
#tip calculator
print("Welcome to the tip calculator!!")
total = float(input("Enter the total bill amount: "))
tip = int(input("Enter how much percentage of bill you would like to give us as a tip: "))
payable_amount = float((tip/100)+total)
members = int(input("Enter total number of members: "))
amount_for_each = payable_amount/members
print(f"Total amount to pay is {payable_amount}")
print(f"Amount payable to each member is {amount_for_each}")
