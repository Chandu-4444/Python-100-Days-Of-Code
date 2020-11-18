from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(height=600, width=800)
screen.title("pong")
screen.tracer(0)

border = Turtle()
border.pencolor("white")
border.setheading(90)
border.penup()
border.goto(0, -300)
while border.ycor() <= 300:
    border.pendown()
    border.fd(10)
    border.penup()
    border.fd(10)



r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
Score = ScoreBoard()


screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    # Detect collision with right paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()

    # Detect when right paddle misses!
    if ball.xcor() > 360:
        ball.reset_position()
        Score.l_point()

    if ball.xcor() < -360:
        ball.reset_position()
        Score.r_point()

    if Score.l_score == 5:
        Score.goto(-250, 230)
        Score.write("Game Point", align="center", font=("Courier", 30, "normal"))
    if Score.r_score == 5:
        Score.goto(250, 230)
        Score.write("Game Point", align="center", font=("Courier", 30, "normal"))

    if Score.l_score > 5:
        Score.clear()
        Score.goto(-200, 0)
        Score.write("You Won!", align="center", font=("Courier", 40, "normal"))
        game_is_on = False

    if Score.r_score > 5:
        Score.clear()
        Score.goto(200, 0)
        Score.write("You Won!", align="center", font=("Courier", 40, "normal"))
        game_is_on = False



















screen.exitonclick()
