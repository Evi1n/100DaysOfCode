# Importing Modules
import math
import time
from tkinter import *
from PIL import ImageTk, Image
from matplotlib.pyplot import text

reps = 0
WORK_MIN = 1
SHORT_BREAK = 1
LONG_BREAK = 1
timer = None

# Define the Reset function
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(title_label, text="Timer")
    check_marks.config(check_marks, text="")
    global reps 
    reps=0

# Define the Start Function
def start_timer():
    global reps
    reps +=1
    work_sec = WORK_MIN * 6
    short_break_sec = SHORT_BREAK * 6
    long_break_sec = LONG_BREAK * 6
    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Break")
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="Break")
    else:
        count_down(work_sec)
        title_label.config(text="Work")

# Define the Countdown 
def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec<10:
        count_sec=f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count -1)
    else:
        start_timer()
        marks = ""
        work_session = math.floor(reps/2)
        for _ in range(work_session):
            marks += "✔"
        check_marks.config(text=marks)

# Window Settings
window = Tk()
window.title("Pomodoro App Made by Eviln")
window.config(bg="#FCE2DB")
window.resizable(width=False, height=False)

# Label Settings
title_label = Label(text="TİMER", fg="#F73D93",bg="#FCE2DB", font=("Courier", 50, "bold"))
title_label.grid(row=0, column=1)

# Image Settings
canvas = Canvas(window, bg="#FCE2DB", highlightthickness=0)
image_cloud = ImageTk.PhotoImage(Image.open("cloud2.png"))
canvas.create_image(0, -60 ,anchor=NW,image=image_cloud)
timer_text = canvas.create_text(180, 130, text="00:00", fill="#F73D93", font=("Courier", 35, "bold"))
canvas.grid(row=1, column=1)

# Button Settings
start_button = Button(text="Start", width=15, command=start_timer).grid(row=2, column=0)
reset_button = Button(text="Reset", width=15, command=reset_timer).grid(row=2, column=2)

# Check Marks Settings
check_marks = Label(text="", fg="#F73D93",bg="#FCE2DB",font=("Courier", 20, "bold"))
check_marks.grid(row=3, column=1)

window.mainloop()