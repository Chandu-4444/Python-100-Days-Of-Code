from tkinter import *
from tkinter import messagebox
import random
import pyperclip


#Password Generator
def generator():
    password_entry.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
    password_list = password_letters+password_numbers+password_symbols
    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)




def save():
    if len(website_entry.get())==0 or len(password_entry.get())==0:
        messagebox.showinfo(title="🚫", message="Empty Fields are Invalid!")

    else:

        is_ok = messagebox.askokcancel(title=website_entry.get(), message=f"Details Entered:\nEmail: {email_entry.get()}\nPassword: {password_entry.get()}\nIs it ok?")
        if is_ok:
            file = open("data.txt", "a")
            file.write(f"{website_entry.get()} | {email_entry.get()} | {password_entry.get()}\n")
            file.close()
            website_entry.delete(0, END)
            password_entry.delete(0, END)









window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=20)

canvas = Canvas(height=200, width=200)
image= PhotoImage(file="lock.png")
canvas.create_image(100, 100, image=image)
canvas.grid(row=0, column=1)

#Labels
website_label= Label(text="Website: ")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username: ")
email_label.grid(row=2, column=0)
password_label = Label(text="Password: ")
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry(width=36)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=36)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "chandrakiran.g19@iiits.in")
password_entry = Entry(width=27)
password_entry.grid(row=3, column=1, columnspan=1)

# Buttons
generate_button = Button(text="Generate", width=5, padx=13, command=generator)
generate_button.grid(row=3, column=2, columnspan=2)
add_button = Button(text= "Add", width=34, command=save)
add_button.grid(row=4, column=1, columnspan=2)



window.mainloop()