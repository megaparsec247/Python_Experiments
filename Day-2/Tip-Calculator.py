print("Welcome to the Tip Calculator")
amount = float(input("Enter the total bill: "))
people = float(input("Enter the total number of people: "))
tip = int(input("Enter the tip percentage(12,15,18): "))

total = (amount/people)*(1+tip/100)
rounded_total = round(total, 2)
print(f"Each person should pay: {rounded_total}")