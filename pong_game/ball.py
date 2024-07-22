from turtle import Turtle
from paddle import Paddle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.penup()

        self.x_move = 10
        self.y_move = 10

    # def move(self):
    #     if self.ycor() >= 450:
    #         self.y_direction = -15
    #
    #     if self.ycor() >= -450:
    #         self.y_direction = 15
    #
    #     if self.direction_to_east:
    #         self.x_direction = 15
    #         self.goto(self.xcor() + self.x_direction, self.ycor() + self.y_direction)
    #     else:
    #         self.x_direction = -15
    #         self.goto(self.xcor() + self.x_direction, self.ycor() + self.y_direction)

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1