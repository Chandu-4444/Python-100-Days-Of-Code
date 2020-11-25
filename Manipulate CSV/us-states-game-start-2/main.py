import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
guessed_states = []
# def Mouse_Click (x, y):  # Prints x, y Coordinates of Mouse Click
#     print(x, y)
#
#
# turtle.onscreenclick(Mouse_Click)
# turtle.mainloop()  # Same as exitonclick()
while len(guessed_states) < 50:
    answer = screen.textinput(title=f"{len(guessed_states)}/50 States correct", prompt="What's another state's name?").title()
    print(answer)
    data = pd.read_csv("50_states.csv")
    states = data.state.to_list()

    if answer == "Exit":
        missing_states = []
        for state in states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("States_Missed.csv", header="")
        break

    if answer in states:
        guessed_states.append(answer)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_row = data[data.state == answer]
        t.goto(float(state_row.x), float(state_row.y))
        t.write(answer)  # t.write(state_row.state.item())

#  states_missed.csv




screen.exitonclick()