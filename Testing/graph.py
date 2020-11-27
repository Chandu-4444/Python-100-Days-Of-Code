from turtle import Turtle, Screen
import random

trt = Turtle()
scr = Screen()
scr.setup(720, 720)

vertices = [(0, -100), (100, 200), (200, 150), (300, 300), (-240, 240), (150, 150)]
edges = [(0,5), (1, 2), (2, 4), (2, 5), (3, 1), (3, 5)]
colors = ["blue", "medium spring green", "lime", "gold", "medium blue", "cyan"]
trt.speed("fastest")
y_start = -320
y_cor = []

scr.tracer(0)
# Drawing Y Coordinates
while y_start <= 320:
    y_cor.append(y_start)
    y_start += 10

for y in y_cor:
    trt.penup()
    trt.goto(-360, y)
    trt.pendown()
    trt.fd(720)



x_cor = []
x_start = 360
trt.rt(90)

while x_start >= -360:
    x_cor.append(x_start)
    x_start -= 10
for x in x_cor:
    trt.penup()
    trt.goto(x, 320)
    trt.pendown()
    trt.fd(640)


trt.setheading(0)
trt.goto(-360, 0)
trt.pensize(5)
trt.fd(720)
trt.penup()

trt.goto(0, -320)
trt.lt(90)
trt.pendown()
trt.fd(640)
trt.penup()
trt.goto(0, 0)


trt.pencolor("red")
trt.hideturtle()
# Plotting Vertices
num=0
for cor in vertices:
    trt.goto(cor[0], cor[1])
    trt.pendown()
    trt.pencolor("blue")
    trt.write(f"{num}", align="left", font=("Courier", 10, "normal"))
    trt.pencolor("red")
    num=num+1
    trt.dot(10)
    trt.penup()



# Plotting Edges
trt.pensize(2)

for edge in edges:
    trt.pencolor(random.choice(colors))
    print(edge)
    trt.penup()
    first_point = edge[0]
    second_point = edge[1]
    trt.goto(vertices[first_point][0], vertices[first_point][1])
    trt.pendown()
    trt.goto(vertices[second_point][0], vertices[second_point][1])
scr.update()





scr.exitonclick()