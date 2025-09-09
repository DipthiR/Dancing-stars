import turtle
import random
import time

# Setup screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("✨ Dancing Stars ✨")

# Create a turtle for stars
star = turtle.Turtle()
star.hideturtle()
star.speed(0)

# Function to draw a star
def draw_star(x, y, size, color):
    star.penup()
    star.goto(x, y)
    star.pendown()
    star.color(color)
    star.begin_fill()
    for _ in range(5):
        star.forward(size)
        star.right(144)
    star.end_fill()

# Colors for stars
colors = ["#FFD700", "#FF69B4", "#ADFF2F", "#87CEEB", "#FFA500"]

# Animate stars
for _ in range(50):  # number of stars
    x = random.randint(-300, 300)
    y = random.randint(-250, 250)
    size = random.randint(10, 30)
    color = random.choice(colors)
    draw_star(x, y, size, color)
    time.sleep(0.1)  # delay for animation

screen.mainloop()
