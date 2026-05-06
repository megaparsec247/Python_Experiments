# import turtle

# timmy = turtle.Turtle()

#attribute is the data that object has
#functions that are  associated with an object or the work it can do is called methods

from turtle import Turtle, Screen
timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.fillcolor("coral")
timmy.forward(100)

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()
