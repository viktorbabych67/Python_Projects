from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("green")
        self.speed("fastest")
        self.penup()
        self.shapesize(0.5, 0.5)

    def location(self):
        x = random.randint(-260, 260)
        y = random.randint(-260, 260)
        return self.goto(x, y)
