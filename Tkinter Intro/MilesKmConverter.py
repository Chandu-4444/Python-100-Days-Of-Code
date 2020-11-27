from tkinter import *
window = Tk()
window.title("Miles to Km Converter")
window.minsize(400, 400)
window.config(pady=20, padx=20)

def button_click():
    ans.config(text=f"{input.get()}")

# Input
input = Entry(width = 20)
input.grid(row=1, column=2)

text1 = Label(text="Miles", font=("Arial", 15, "normal"))
text1.grid(row=1, column=3)

text2 = Label(text = "Equals: ", font=('Arial', 15, "normal"))
text2.grid(row=2, column=0)

ans = Label(text="0", font=("Arial", 15, "normal"))
ans.grid(row=2, column=2)

text3 = Label(text="Km", font=("Arial", 15,"normal"))
text3.grid(row=2, column=3)

button = Button(text="Calculate", command = button_click)
button.grid(row=3, column=2)









window.mainloop()