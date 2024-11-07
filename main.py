import turtle
from turtle import Turtle, Screen
import random

# Initialize the turtle and screen
tim = Turtle()
tim.shape("arrow")
screen = Screen()
screen.colormode(255)  # Set the color mode to RGB

directions = [0, 90, 180, 270]

# Function to generate a random color
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

# Move the turtle in random directions with random colors
for _ in range(200):
    tim.color(random_color())  # Set random color
    tim.forward(30)
    tim.setheading(random.choice(directions))
    tim.pensize(15)
    tim.speed(0)

# Exit on click
screen.exitonclick()
