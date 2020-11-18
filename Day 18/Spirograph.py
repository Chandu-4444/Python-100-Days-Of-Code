import turtle as t
import random
t.colormode(255)
trt = t.Turtle()
trt.speed("fastest")
for i in range(180):
    trt.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    trt.circle(100)
    trt.rt(2)

scr= t.Screen()
scr.exitonclick()
