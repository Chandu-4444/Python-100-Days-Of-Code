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

# Radio buttons
COLOR1 = "Blue"
COLOR2 = "Gold"
COLOR3 = "Red"

# Radiobutton Callback

def radCall():
    radSel = radVar.get()
    if radSel == 1:
        window.config(background=COLOR1)
    elif radSel == 2:
        window.config(background=COLOR2)
    elif radSel == 3:
        window.config(background=COLOR3)






radVar = tk.IntVar()

rad1 = tk.Radiobutton(window, text=COLOR1, variable=radVar, value=1, command=radCall)
rad1.grid(column=0, row=5, sticky=tk.W, columnspan=3)

rad2 = tk.Radiobutton(window, text=COLOR2, variable=radVar, value=2, command=radCall)
rad2.grid(column=1, row=5, sticky=tk.W, columnspan=3)

rad3 = tk.Radiobutton(window, text=COLOR3, variable=radVar, value=3, command=radCall)
rad3.grid(column=2, row=5, sticky=tk.W, columnspan=3)


window.mainloop()
