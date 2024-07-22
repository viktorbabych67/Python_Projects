from turtle import Turtle, Screen
import random
import turtle

# turtle = turtle.Turtle()
#
# turtle.shape("turtle")
#
# for i in range(4):
#     turtle.forward(100)
#     turtle.right(90)
#
# for i in range(20):
#     turtle.forward(5)
#     turtle.right(90)


# turtle.teleport(-360)
#
# for i in range(50):
#     turtle.pendown()
#     turtle.forward(8)
#     turtle.penup()
#     turtle.forward(8)

numb_sides = 3
colors = ["blue", "orange", "deep sky blue", "magenta", "green"]
current_color = 0
turtle.speed(5)
for i in range(numb_sides, 8):
    angle = 360 / numb_sides
    turtle.pencolor(colors[current_color])
    for s in range(numb_sides):
        turtle.right(angle)
        turtle.forward(50)
    numb_sides += 1
    current_color += 1

#####################################################################################################################


# # Set up the screen and turtle
# screen = turtle.Screen()
# screen.colormode(1.0)  # Set color mode to 1.0 to accept float RGB values
#
# tim = turtle.Turtle()
# tim.speed(1)
#
# tim.color("green")
# tim.speed(2)
#
# turtle.pensize(15)
#
# direction = [0, 90, 180, 270]
# colors = ["blue", "orange", "deep sky blue", "magenta", "green"]
#
#
# def random_color():
#     r = random.randint(0, 255) / 255.0
#     g = random.randint(0, 255) / 255.0
#     b = random.randint(0, 255) / 255.0
#     randoms = (r, g, b)
#     return randoms
#
#
# for i in range(50):
#     turtle.color(random_color())
#     turtle.setheading(random.choice(direction))
#     turtle.forward(random.randint(20, 100))
#
# screen = Screen()
# screen.exitonclick()

####################################################################\\\

# Set up the screen and turtle

# screen = turtle.Screen()
# screen.colormode(255)  # Set color mode to 1.0 to accept float RGB values
#
#
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     randoms = (r, g, b)
#     return randoms
#
#
# tim = turtle.Turtle()
# tim.speed(20)
# count = 0
#
# run = True
# while run:
#     tim.color(random_color())
#     tim.circle(100)
#     tim.setheading(tim.heading()+10)
#     if tim.heading() == 0:
#         run = False


# run = True
# while run:
#     tim.color(random_color())
#     tim.circle(100)
#     tim.left(count)
#     count += 0.5
#     if count == 15:
#         run = False






screen = Screen()
screen.exitonclick()