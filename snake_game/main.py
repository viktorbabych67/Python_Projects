from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food
from score import Score

score_hit = Score()
snake_food = Food()
snake = Snake()
screen = Screen()
screen.setup(600, 600)

screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")

game_is_on = True

snake_food.location()


while game_is_on:

    screen.update()
    time.sleep(0.1)
    snake.move()
    print(snake.head.position())
    print(snake.segments)

    if snake.head.distance(snake_food) < 15:
        snake.add_tail()
        snake_food.location()
        score_hit.num_of_eaten()

    if snake.head.xcor() >= 300.0 or snake.head.xcor() == -300.0 or snake.head.ycor() >= 300.0 or snake.head.ycor() == -300.0:
        score_hit.game_over()
        game_is_on = False

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score_hit.game_over()
            game_is_on = False

screen.exitonclick()
