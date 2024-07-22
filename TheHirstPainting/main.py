# import colorgram
#
# colors = colorgram.extract('image.jpg', 45)

# colors_list = []
#
# for i in colors:
#     rgb = str(i.rgb)
#
#     rgb_striped = rgb.replace("Rgb(", "").replace(")", "").replace("r=", "").replace("g=", "").replace("b=", '')
#     r, g, b = map(int, rgb_striped.split(", "))
#     result = (r, g, b)
#     colors_list.append(result)
#
# print(colors_list)

import turtle
import random

col = [(226, 232, 239), (1, 9, 30), (242, 235, 241), (121, 95, 41), (72, 32, 22), (238, 212, 72), (220, 81, 59),
       (226, 117, 100), (93, 1, 21), (178, 140, 170), (150, 92, 115), (35, 90, 26), (7, 155, 73), (205, 63, 91), (168, 129, 77), (1, 64, 147),
       (3, 78, 28), (4, 220, 218), (220, 178, 218), (79, 135, 179), (128, 156, 178), (80, 110, 136), (121, 186, 164), (10, 214, 221), (120, 15, 34),
       (243, 205, 7), (133, 223, 208), (229, 173, 165), (186, 190, 200), (70, 72, 43), (126, 225, 230), (88, 49, 44)]

tim = turtle.Turtle()
screen = turtle.Screen()
screen.colormode(255)

tim.teleport(-200)
tim.penup()
tim.sety(-200)
tim.pendown()
tim.speed(150)
for r in range(10):
    tim.teleport(-200)

    for i in range(10):
        tim.pencolor(col[random.randint(1, 30)])
        tim.dot(20)
        tim.penup()
        tim.forward(50)
        tim.pendown()
    tim.penup()
    tim.teleport(tim.sety(tim.ycor() + 50))
    tim.pendown()

screen = turtle.Screen()
screen.exitonclick()

#################################
# rgb_strip = test.strip("Rgb()")
#
# parts = rgb_strip.split(", ")
#
# r = int(parts[0].split("=")[1])
# g = int(parts[1].split("=")[1])
# b = int(parts[2].split("=")[1])
#################################
