# Install turtle using pip install turtle

from turtle import *
from random import randint

# Creating unique instances of the Turtle class
john = Turtle()
bob = Turtle()
sally = Turtle()

# Assigning properties to our Turtles 
john.color('red')
john.shape('turtle')

bob.color('green')
bob.shape('turtle')

sally.color('blue')
sally.shape('turtle')


# Giving our Turtles instructions to move to the starting position

john.penup()
john.goto(-160, 100)
john.pendown()

bob.penup()
bob.goto(-160, 70)
bob.pendown()

sally.penup()
sally.goto(-160, 40)
sally.pendown()

# Giving our Turtles instructions to move 'forwards' and race

for movement in range(100):
    john.forward(randint(1, 5))
    bob.forward(randint(1, 5))
    sally.forward(randint(1, 5))

input('Press Enter to close')
