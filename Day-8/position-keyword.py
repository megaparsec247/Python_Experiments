#function with more than one input

def greet_with(name, location):
    print(f"Hello {name}")
    print(f"I love {location}")

name = input("What is your name: ")
location = input("Where do you live: ")

greet_with(name, location) #positional arguement

greet_with(location = "Shimla", name = "Ram") #keyword arguement