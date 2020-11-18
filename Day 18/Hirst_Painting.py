import turtle as t
import random
t.colormode(255)
trt = t.Turtle()
trt.speed("fastest")
trt.penup()  # Don't draw
trt.hideturtle()  # Hide Turtle
colors = [(246, 244, 242), (234, 240, 246), (239, 246, 243), (247, 239, 242), (132, 166, 204), (220, 149, 107), (198, 135, 148), (31, 41, 61), (41, 105, 154), (142, 183, 162), (163, 60, 49), (237, 212, 91), (149, 60, 68), (213, 81, 70), (53, 111, 91), (172, 27, 33), (159, 32, 29), (235, 167, 157), (34, 60, 55), (15, 99, 71), (231, 161, 166), (170, 188, 221), (56, 52, 48), (53, 44, 49), (195, 98, 107), (32, 60, 109), (106, 127, 159), (174, 200, 188), (33, 151, 209), (65, 66, 57), (155, 203, 224), (105, 140, 127), (40, 71, 74), (239, 183, 13)]
trt.setheading(220)
trt.forward(300)
trt.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots+1):
    trt.dot(20, random.randint(0,255), random.randint(0,255), random.randint(0,255))
    trt.forward(50)

    if dot_count % 10 == 0:
        trt.setheading(90)
        trt.forward(50)
        trt.setheading(180)
        trt.forward(500)
        trt.setheading(0)

scr = t.Screen()
scr.exitonclick()
