from turtle import Screen
from turtle import Turtle
from snake import Snake
from food import Food
from score_board import ScoreBoard
import time

screen = Screen()
difficulty = int(screen.textinput(title="Welcome!", prompt="Enter Your preferred difficulty? (1-10): "))
if difficulty not in range(1, 11):
    warning = Turtle()
    warning.color("red")
    warning.hideturtle()
    warning.write(f"You entered wrong choice! Setting default to 1", align="center", font=("Courier", 10, "normal"))
    # warning.clear()
    time.sleep(2)
    warning.clear()
    difficulty = 1

screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)  # Stop all screen activities from showing
segments = []

snake = Snake()
food = Food()

scoreboard = ScoreBoard()
SPEED = [0.1, 0.099, 0.089, 0.079, 0.069, 0.059, 0.049, 0.039, 0.029, 0.019]


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(SPEED[difficulty])
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        scoreboard.reset()
        snake.reset()
    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()
