from turtle import Turtle

ALIGNMENT = "left"
FONT = ("Arial", 50, "bold")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.point_1 = 0

        self.color("white")
        self.hideturtle()
        self.penup()

    def add_score_1(self):
        self.point_1 += 1

    def first_score(self):
        self.goto(-50, 230)
        self.write(self.point_1, align="right", font=FONT)

    def second_score(self):
        self.goto(90, 230)
        self.write(self.point_1, align="right", font=FONT)
