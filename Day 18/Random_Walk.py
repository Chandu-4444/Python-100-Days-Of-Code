import turtle as t
import random
t.colormode(255)
trt = t.Turtle()
# colors = ["pale goldenrod", "magenta", "wheat", "yellow", "deep pink", "medium blue", "dim gray", "lawn green", "orange red", "purple", "peru", "cyan"]
dire = [0, 90, 180, 270]
trt.speed("fast")
trt.pensize(10)

for i in range(200):
    # trt.color(random.choice(colors))
    trt.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    trt.forward(25)
    trt.setheading(random.choice(dire))
    if trt.pos()[0] <-400 or trt.pos()[1]>300 or trt.pos()[1]<-300 or trt.pos()[0]>400 :
        trt.color("")
        trt.setpos(0,0)




scr = t.Screen()
scr.exitonclick()
