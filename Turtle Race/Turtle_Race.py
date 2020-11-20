import turtle as t
import random

scr = t.Screen()
scr.setup(500, 400)  # Set screen size
user_bet = scr.textinput(title="Make you bet", prompt="Which turtle will win the race? Enter Colour: ")
colors = ["red", "blue", "green", "yellow", "orange", "violet"]
y_position = [-100, -60, -20, 20, 60, 100]
finished = True
list_turtles=[]

for turtle_index in range(0, 6):
    tim = t.Turtle("turtle")
    tim.penup()
    tim.color(colors[turtle_index])
    # tim.shape("turtle")
    tim.goto(x=-230, y=y_position[turtle_index])
    list_turtles.append(tim)

if user_bet:
    finished = False

while not finished:
    for turtle in list_turtles:
        if turtle.xcor() > 230:
            finished = True
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You,ve won! The {winning_color} turtle is the winner! ")
            else:
                print(f"You,ve lost! The {winning_color} turtle is the winner!")
        rand_distance = random.randint(0, 7)
        turtle.fd(rand_distance)
scr.exitonclick()
