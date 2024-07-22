from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0), (-60, 0), (-80, 0), (-100, 0), (-120, 0)]


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def move(self):
        for seg_numb in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_numb - 1].xcor()
            new_y = self.segments[seg_numb - 1].ycor()
            self.segments[seg_numb].goto(new_x, new_y)
        self.head.forward(10)

    def create_snake(self):
        for i in STARTING_POSITIONS:
            segment = Turtle("square")
            segment.color("white")
            segment.penup()
            segment.goto(i)
            self.segments.append(segment)

    def up(self):
        if self.head.heading() != 270:
            self.segments[0].setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def add_tail(self):
        last_segment = self.segments[-1]
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(last_segment.position())
        self.segments.append(new_segment)


