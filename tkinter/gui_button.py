import tkinter as tk
from tkinter import ttk
window = tk.Tk()
window.title("Window")

label = ttk.Label(window, text="A Label")
label.grid(column=0, row=0, padx=20, pady=20)

def click_me():
    action.configure(text = "Clicked Me!")
    label.configure(foreground="red")
    label.configure(text="A Red Label")

action = ttk.Button(window, text="Click Me!", command=click_me)
action.grid(column=1, row=0, padx=10)

window.mainloop()
