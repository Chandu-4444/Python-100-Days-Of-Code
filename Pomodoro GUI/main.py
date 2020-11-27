from tkinter import *
import time
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME="Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=0
timer = None
# Reset
def reset_timer():
    window.after_cancel(timer)  # Cancels previous timer
    canvas.itemconfig(timer_text, text="00:00")
    title.config(text="Timer")
    tick.config(text="")
    global reps
    reps=0




# Counter Mechanism
def start_timer():
    global reps
    reps+=1
    work_sec = WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN*60
    long_break_sec=LONG_BREAK_MIN*60

    if reps % 8==0:
        count_down(long_break_sec)
        title.config(text="Break", fg=RED)
    elif reps %2 ==0:
        count_down(short_break_sec)
        title.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        title.config(text="Work", fg=GREEN)





# Counter
def count_down(count):
    min = count//60
    sec = count % 60
    # For displaying 00 in seconds
    if sec == 0 or sec < 10:
        sec = "0"+str(sec)  # sec = f"0{sec}"

    canvas.itemconfig(timer_text, text=f"{min}:{sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        mark = ""
        # 2 Reps Gives  One Session (Work, Break = One Complete Session)
        for _ in range(reps//2):
            mark+="✔"
        tick.config(text=mark)






window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


#
# def do_something(thing):
#     print("Done Something! "+thing)
#
#
# window.after(1000, do_something, "This is a thing(I'm Optional)")

title = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
title.grid(row=0, column=1)


canvas = Canvas(width=200, height=200, bg=YELLOW, highlightthickness=0)  # For Displaying Image, highlightthickness=0
# removes border between png and window
image = PhotoImage(file="apple.png")
canvas.create_image(100, 100, image= image)
timer_text = canvas.create_text(100, 120, text="0", fill="white", font=(FONT_NAME, 25, "bold"))
canvas.grid(row=1, column=1)

start_text = Button(text = "Start", bg=YELLOW, command=start_timer)  # Can Remove that color around by highlightthickness=0, But be it that
# way
start_text.grid(row=2, column=0)

tick = Label(text="", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 30))
tick.grid(row=2, column=1)

reset_text = Button(text="Reset", bg=YELLOW, command=reset_timer)
reset_text.grid(row=2, column=2)




window.mainloop()




