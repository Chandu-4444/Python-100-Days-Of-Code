import smtplib
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

def send_me():
    mess = message.get("1.0", tk.END)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=from_email.get(), password=password.get())
        connection.sendmail(
            from_addr=from_email.get(),
            to_addrs=to_mail.get(),
            msg=f"Subject:{subject.get()}\n\n{mess}")


Window = tk.Tk()
Window.title("Email")
Window.configure(pady=20, padx=10)


from_frame = ttk.LabelFrame(Window, text="From Details")
from_frame.grid(row=0, column=0, padx=5, pady=5)

ttk.Label(from_frame, text="From: ").grid(row=0, column=0)
from_email = tk.StringVar()
from_email = ttk.Entry(from_frame, width=20, textvariable=from_email)
from_email.focus()
from_email.grid(row=0, column=1)
ttk.Label(from_frame,text="Password: ").grid(row=1, column=0)
password = ttk.Entry(from_frame,width=20)
password.grid(row=1, column=1)



to_frame = ttk.LabelFrame(Window, text="To Details")
to_frame.grid(row=1, column=0, padx=3, pady=5)


ttk.Label(to_frame, text="To: ").grid(row=0, column=0)
to_mail = ttk.Entry(to_frame, width=25)
to_mail.grid(row=0, column=1, padx=5, pady=5)


message_frame = ttk.LabelFrame(Window, text="Message")
message_frame.grid(row=3, column=0)
ttk.Label(message_frame,text="Subject: ").grid(row=0, column=0)
subject = ttk.Entry(master=message_frame,width=23)
subject.grid(row=0, column=1)
ttk.Label(message_frame, text="Message").grid(row=1, column=0)
message = tk.Text(message_frame, width=30, height=10,wrap=tk.WORD)
message.grid(row=2, column=0,columnspan=2)


def show():
    print(from_email.get())
    print(to_mail.get())
    print(password.get())
    print(subject.get())
    print(message.get("1.0", tk.END))
send = ttk.Button(text="Send", command=send_me)
send.grid(row=4,column=0)









Window.mainloop()