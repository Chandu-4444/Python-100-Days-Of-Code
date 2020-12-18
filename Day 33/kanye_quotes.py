import requests
from tkinter import *

def quote():
    response = requests.get("https://api.kanye.rest")
    response.raise_for_status()

    data = response.json()
    canvas.itemconfig(quote_text, text=data["quote"])

window = Tk()
window.title("Kanye says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_image = PhotoImage(file="yellow2.png")
canvas.create_image(150, 207, image=background_image)
quote_text = canvas.create_text(150, 207, text="", width=250, font=("Arial", 12, "italic"))
canvas.grid(row=0, column=0)

button = Button(text="Motivate!", command=quote)
button.grid(row=1, column=0)
window.mainloop()
