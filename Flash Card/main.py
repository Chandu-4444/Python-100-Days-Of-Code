from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"
current_card={}
to_learn={}

try:
    data = pandas.read_csv("words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("Hindi-En.csv")
    to_learn = original_data.to_dict(orient="records")

else:
    to_learn = data.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="Hindi", fill="black")
    canvas.itemconfig(card_text, text=current_card["Hindi"], fill="black")
    canvas.itemconfig(back, image=card_front)
    flip_timer = window.after(3000, func=flip_card) # Start new flip timer from current moment




def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_text, text=current_card["English"], fill="white")
    canvas.itemconfig(back, image = card_back)

def known():
    global data
    to_learn.remove(current_card)
    next_card()
    data = pandas.DataFrame(to_learn)
    data.to_csv("words_to_learn.csv", index=False)





window=Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=500, height= 400)
card_front = PhotoImage(file="white1.png")
card_back = PhotoImage(file="dark.png")
back = canvas.create_image(450, 450, image=card_front)
card_title = canvas.create_text(250, 100,text="Title", font=("Ariel", 40, "italic"))
card_text = canvas.create_text(250, 250,text="word", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR)
canvas.grid(row=0, column=0, columnspan=2)

cross_image = PhotoImage(file="cross.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

check_image=PhotoImage(file="correct.png")
known_button= Button(image=check_image, command=known)
known_button.grid(row=1, column=1)

next_card()

window.mainloop()