from turtle import Turtle, Screen

trt = Turtle()
trt.pensize(10)

def move_forward():
    trt.fd(10)


scr = Screen()
scr.listen()
scr.onkey(key="space", fun=move_forward)
scr.exitonclick()
