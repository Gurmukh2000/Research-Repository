import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")

# Create a turtle object
t = turtle.Turtle()

# Set the speed of the turtle
t.speed(0)
t.width(3)  # Set the thickness of the lines

# Function to draw a star


def draw_star(size):
    for i in range(5):
        t.forward(size)
        t.right(144)


# Set the initial position of the turtle
t.penup()
t.goto(-500, 0)
t.pendown()

# Set the size of the star
size = 100

# Draw the star with 5 different colors
for _ in range(5):
    # Generate a random color
    color = (random.random(), random.random(), random.random())
    t.color(color)
    draw_star(size)
    t.penup()
    t.forward(200)
    t.pendown()

# Hide the turtle and display the result
t.hideturtle()
turtle.done()
