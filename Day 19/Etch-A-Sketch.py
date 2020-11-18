import turtle as t

trt = t.Turtle()


def move_forward():
    trt.fd(10)


def move_backward():
    trt.bk(10)


def turn_left():
    new_heading = trt.heading()+10
    trt.setheading(new_heading)


def turn_right():
    new_heading = trt.heading()-10
    trt.setheading(new_heading)


def clear_screen():
    trt.clear()
    trt.penup()  # To avoid turtle drawing during back to home
    trt.home()
    trt.pendown()


trt.pensize(5)

scr = t.Screen()
scr.listen()
scr.onkey(move_forward, "w")
scr.onkey(move_backward, "s")
scr.onkey(turn_left, "a")
scr.onkey(turn_right, "d")
scr.onkey(clear_screen, "c")
scr.exitonclick()
