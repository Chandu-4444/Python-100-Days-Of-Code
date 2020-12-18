import tkinter as tk
from tkinter import ttk
window = tk.Tk()
window.title("Window")



def click_me():
    action.configure(text = "Clicked Me! "+ name_entered.get())


action = ttk.Button(window, text="Click Me!", command=click_me)
action.grid(column=1, row=1)

ttk.Label(window, text="Enter Name: ").grid(column=0, row=0)

name = tk.StringVar()
name_entered = ttk.Entry(window, width=12, textvariable=name)
name_entered.focus()
name_entered.grid(column=0, row=1)

window.mainloop()
