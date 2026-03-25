def greet():
    print("Hello")
    print("Good Morning")
    print("Have a great day")

 
def greet_with_name(name):   #parameter
    print(f"Hello {name}")
    print("Good Morning")
    print("Have a great day")   

name = input("What is your name? ") #arguement

greet_with_name(name)