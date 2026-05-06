try:
    age = int(input("Enter your age: "))
except ValueError:
    print("enter a numerical value.")
    age = int(input("Enter your age: "))

if age>18:
    print(f"You can drive at age {age}")
