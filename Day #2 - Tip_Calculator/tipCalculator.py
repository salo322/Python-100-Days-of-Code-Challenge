# Tip Calculator
print("Welcome to the tip calculator")

total_bill = input("What was the total bill? $ ")
total_tip = input("How much tip would you like to give 10, 12 or 15? ")
total_people = input("How many people should split the bill? ")

total_bill_to_number = float(total_bill)
total_tip_to_number = int(total_tip)
total_people_to_number = int(total_people)

each_person_pay_amount = (total_bill_to_number + total_tip_to_number) / total_people_to_number

print(f"Each person should pay: $ {round(each_person_pay_amount, 2)}")






