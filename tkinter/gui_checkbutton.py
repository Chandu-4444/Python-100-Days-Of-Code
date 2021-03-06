import tkinter as tk
from tkinter import ttk
window = tk.Tk()
window.title("Window")


def click_me():
    action.configure(text = "Clicked Me! "+ name.get()+" "+number_chosen.get()+" "+str(chVarUn.get()))


action = ttk.Button(window, text="Click Me!", command=click_me)
action.grid(column=2, row=1)

ttk.Label(window, text="Choose: ").grid(column=1, row=0)
number = tk.StringVar()
number_chosen = ttk.Combobox(window, width=12, textvariable=number)
number_chosen["values"] = (1, 2, 3, 5, 9)
number_chosen.grid(column=1, row=1)
number_chosen.current(0)

# Checkbuttons

chVarDis = tk.IntVar()
check1 = tk.Checkbutton(window, text="Disabled", variable = chVarDis, state="disabled")
check1.select()
check1.grid(column=0, row=4, sticky=tk.W)

chVarUn = tk.IntVar()
check2 = tk.Checkbutton(window, text="Unchecked", variable=chVarUn, command=click_me)
check2.deselect()
check2.grid(column=1, row=4, sticky=tk.W)

chVarEn = tk.IntVar()
check3 = tk.Checkbutton(window, text="Enabled", variable=chVarEn)
check3.select()
check3.grid(column=2, row=4, sticky=tk.W)


ttk.Label(window, text="Enter Name: ").grid(column=0, row=0)
name = tk.StringVar()
name_entered = ttk.Entry(window, width=12, textvariable=name)
name_entered.focus()
name_entered.grid(column=0, row=1)

window.mainloop()
