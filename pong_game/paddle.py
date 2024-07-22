from turtle import Turtle


class Paddle:
    def __init__(self):
        self.paddle = Turtle("square")
        self.paddle.color("white")
        self.paddle.speed(0)

    def create_paddle(self, start_pos):
        self.paddle.penup()
        self.paddle.shapesize(5, 1)
        self.paddle.goto(start_pos)

    def up(self):
        if self.paddle.ycor() <= 270:
            self.paddle.goto(self.paddle.xcor(), self.paddle.ycor() + 20)

    def down(self):
        if self.paddle.ycor() >= -260:
            new_y = self.paddle.ycor() - 20
            self.paddle.goto(self.paddle.xcor(), new_y)

    def position(self):
        return self.paddle.position()