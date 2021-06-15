# 100 Days Of Code - Day 2 Tip Calculator

print("Welcome to the Tip Calculator")
bill = float(input("What is the total bill? $"))
tip = int(input("What Percent tip would you like to add? "))
people = int(input("How Many people in your group? "))

tip = tip / 100
tip_value = bill * tip
bill_tip = float((bill * tip) +bill)
shared_tip = float(tip_value / people)
shared_cost = float(bill_tip / people)

print(f"The Tip will be ${tip_value:.2f}")
print(f"The total bill with tip is ${tip_value:.2f}")
print(f"Each person's part of the tip is ${shared_tip:.2f}")
print(f"Each person should pay ${shared_cost:.2f}")
