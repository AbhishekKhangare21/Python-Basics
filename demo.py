print('Welcome to the tip calculator!')
bill = float(input("What as the total bill? $"))
tip = input("How much tip would you like to give? 10, 12, or 15? ")
people = int(input("How many people to split the bill?"))
bill_with_tip = bill * (1 + tip / 100)


print(bill_with_tip);