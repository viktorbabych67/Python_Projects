from turtle import Turtle, Screen
from score import Score
from ball import Ball
import time
from paddle import Paddle

# STARTING_POSITIONS_1 = [(420, 40), (420, 20), (420, 0), (420, -20)]
# STARTING_POSITIONS_2 = [(-430, 40), (-430, 20), (-430, 0), (-430, -20)]

STARTING_POSITIONS_1 = (420, 0)
STARTING_POSITIONS_2 = (-430, 0)

paddle_right = Paddle()
paddle_left = Paddle()

ball = Ball()
screen = Screen()
middle_line = Turtle()
show_score_1 = Score()
show_score_2 = Score()

screen.tracer(0)

# Set the screen
screen.bgcolor("black")
screen.setup(900, 600)

screen.listen()
screen.onkeypress(paddle_left.up, "w")
screen.onkeypress(paddle_left.down, "s")

screen.onkeypress(paddle_right.up, "Up")
screen.onkeypress(paddle_right.down, "Down")



# Set the paddles
paddle_right.create_paddle(STARTING_POSITIONS_1)
paddle_left.create_paddle(STARTING_POSITIONS_2)

# Move the paddle


# Set the middle dashed line
middle_line.color("white")
middle_line.hideturtle()
middle_line.pensize(4)
middle_line.penup()
# time.sleep(0.1)
middle_line.goto(0, -270)
middle_line.setheading(90)

for i in range(20):
    middle_line.pendown()
    middle_line.forward(15)
    middle_line.penup()
    middle_line.forward(15)
game_on = True
while game_on:

    # if ball.distance(paddle_right.position()) <15:
    #     ball.direction_to_east = False
    # if ball.distance(paddle_left.position()) < 15:
    #     ball.direction_to_east = True

    # Detect collision with wall
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_y()

    # Detect collision with paddles
    if (ball.distance(paddle_right.position()) < 50 and ball.xcor() > 390) or (ball.distance(paddle_left.position()) < 50 and ball.xcor() < -390):
        ball.bounce_x()

    if ball.xcor() >= 470:
        show_score_1.add_score_1()
        print("Goal!!!")

    if ball.xcor() < -490:
        show_score_2.add_score_1()

    # Display the scores
    show_score_1.clear()
    show_score_2.clear()
    show_score_1.first_score()
    show_score_2.goto(90, 230)
    show_score_2.write(show_score_2.point_1, align="right", font=("Arial", 50, "bold"))

    if ball.xcor() >= 470 or ball.xcor() < -490:
        ball.goto(0, 0)
    ball.move()
    ball.speed(0)
    screen.update()
    time.sleep(0.1)

screen.exitonclick()
