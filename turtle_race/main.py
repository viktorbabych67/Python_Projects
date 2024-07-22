import turtle
from turtle import Turtle, Screen
import random
import tkinter.messagebox

screen = Screen()
screen.setup(500, 400)

user_bet = screen.textinput("Make your bet", "Which turtle will win the race? Enter a color: ")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]

y = [-70, -40, -10, 20, 50, 80]
all_turtles = []


for index_turtle in range(0, 6):
    tim = Turtle(shape="turtle")
    tim.color(colors[index_turtle])
    tim.penup()
    tim.goto(-230, y[index_turtle])
    all_turtles.append(tim)
    tim.speed(0)

print(all_turtles[0].xcor())
is_race_on =False
if user_bet:
    is_race_on = True

while is_race_on:
    for inx_turtle in range(0, 6):
        random_distance = random.randint(0, 10)
        all_turtles[inx_turtle].setx(all_turtles[inx_turtle].xcor() + random_distance)
    for i in all_turtles:
        if i.xcor() >= 230:
            if user_bet == i.color()[0]:
                bet = f"You guess was {user_bet}. You lost!"

            bet = f"Your guess was {user_bet}. You win!."
            # print(f"The winner is {i.color()[0]}. {bet}")
            tkinter.messagebox.showinfo("Race Result", f"The winner is {i.color()[0]}. {bet}")
            is_race_on = False
screen.exitonclick()
