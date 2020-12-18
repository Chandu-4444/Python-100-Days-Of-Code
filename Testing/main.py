import  mysql.connector
from mysql.connector import errorcode
from tkinter import *
from tkinter import messagebox

def stop():
    global window
    window.quit()



# def connect():
#     #if len(user_entry.get())!=0 and len(pass_entry)!=0:
#     conn = mysql.connector.connect(user=user_entry.get(), password=pass_entry.get(), host='localhost' )
#     cursor = conn.cursor()
#     global window
#     window.quit()
#     messagebox.showinfo(title="Success!", message="Connected to Server💡")
#     conn.close()

    #tu = cursor.execute("SHOW DATABASES")
    #print("Databases: ")
    #for _ in cursor:
        #print(_)
    #cursor.execute("USE iiits")
    #cursor.execute("SELECT * FROM test")
    #for a, b in cursor:
        #print(f"{a} {b}")
            # cursor.execute("CREATE TABLE test1 (id int, name varchar(30))")
            # cursor.execute("show tables")
            # for tables in cursor:
                # print(tables)
    # except mysql.connector.Error as err:
    #     if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    #         print("Wrong Credentials!")
    #     elif err.errno == errorcode.ER_BAD_DB_ERROR:
    #         print("Database doesn't exist!")
    #     else:
    #         print(err)
    #
    # else:
    #     conn.close()

def manipulate():
    messagebox.showinfo(title="Continuing", message="Proceeding...")
    window.title("Server: localhost")




def connect():
    if user_entry.get() == "l" and pass_entry.get()=="l":
        pass_entry.destroy()
        password.destroy()
        user_entry.destroy()
        user.destroy()
        connect_button.destroy()
        window.title("Proceed to connect?")
        continue_button = Button(text = "Continue", command = manipulate, padx=20)
        continue_button.grid(row=0, column=0)
        cancel = Button(text="Cancel", padx=20, command = window.quit)
        cancel.grid(row=0, column=1)
        






window = Tk()
window.title("Database Manipulation")
window.config(padx=20, pady=50)

user = Label(text="User: ")
user.grid(row = 0, column=1)
user_entry = Entry(width=30)
user_entry.grid(row=0, column=2)
user_entry.focus()
password = Label(text="Password: ")
password.grid(row=1, column=1)
pass_entry = Entry(width = 30)
pass_entry.grid(row=1, column=2)


connect_button = Button(text="connect", command = connect)
connect_button.grid(row=2, column=0, columnspan=2)
window.mainloop()