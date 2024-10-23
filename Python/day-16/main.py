#method 1
#import turtle 
#timmy = turtle.Turtle()

# method 2(we will use it more)
from turtle import Turtle , Screen
timmy = Turtle()
timmy.shape("turtle")
timmy.color("black", "red")
timmy.penup()
timmy.forward(100)
my_screen = Screen()
my_screen.canvheight = 300
my_screen.canvwidth = 300
my_screen.exitonclick()




