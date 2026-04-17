def add(n1,n2):
    return n1+n2
def subtract(n1,n2):
    return n1-n2
def divide(n1,n2):
    return n1/n2
def multiply(n1,n2):
    return n1*n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

# continue_operations = True
# answer = []
# while continue_operations:  
#     if operator == "+":
#         answer = operations["+"](n1,n2)
#     elif operator == "-":
#         answer = operations["-"](n1,n2)
#     elif operator == "*":
#         answer = operations["*"](n1,n2)
#     elif operator == "/":
#         answer = operations["/"](n1,n2)

#     n1 = int(input("Enter the first number: "))
#     operator = input("Which operation do you want to perform?(+,-,*,/): ")
#     n2 = int(input("Enter the second number: "))
#     continue_program = input("Do you want to continue working on the previous result?(y,n)").lower()
#     if continue_program == "y":
        
#         n1 = answer
#     else: 
#         continue_operations = False

def calculator(): 
    should_accumulate = True
    
    num1 = float(input("What is the first number? "))

    while should_accumulate:
        for symbol in operations:
            print(symbol)
        operations_symbol = input("Pick an operation: ")
        num2 = float(input("What is the second number? "))
        answer = operations[operations_symbol](num1,num2)
        print(f"{num1} {operations_symbol} {num2} = {answer}")

        choice = input  (f"Type 'y' to continue calculating with {answer} or type 'n' to start a new calculation: " )

        if choice == "y":
            num1 = answer
        else: 
            should_accumulate = False
            print ("\n" *20)
            calculator()  

calculator()