# Import Modules
from tkinter import *
import pandas
import random

data = pandas.read_csv("word_list.csv")
to_learn = {}
current_card = {}

try:
    data = pandas.read_csv("words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("word_list.csv")
    print(original_data)
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


#----------------------- FUNCTIONS -----------------------#
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card, fill="#ff9cda")
    canvas.itemconfig(card_title, text="English")
    canvas.itemconfig(card_word, text=current_card["English"])
    flip_timer = window.after(3000, func=flip_card)

def known_clicked():
    to_learn.remove(current_card)
    print(len(to_learn))
    data = pandas.DataFrame(to_learn)
    data.to_csv("words_to_learn.csv", index=False)
    next_card()

def flip_card():
    canvas.itemconfig(card, fill="#749eff")
    canvas.itemconfig(card_title, text="Turkish")
    canvas.itemconfig(card_word, text=current_card["Turkish"])


#----------------------- UI SETTINGS -----------------------#

# Window Settings
window = Tk()
window.config(padx=50, pady=50, bg="#dac8e4")
window.resizable(width=False, height=False)
window.title("Flashly")
flip_timer = window.after(3000, func=flip_card)

# Canvas Settings
canvas = Canvas(width=500, height=300, highlightthickness=0)
card = canvas.create_rectangle(0, 0, 500, 300,fill="#ff9cda")
card_title = canvas.create_text(240, 70,text="", font=("Courier", 35, "bold"))
card_word = canvas.create_text(240, 160, text="", font=("Courier", 45, "italic"))
canvas.grid(row=0, column=0, columnspan=2)

empty = Label(bg="#dac8e4")
empty.grid(row=1)

# Button Settings
known_button = Button(text="✔", font=("Ariel", 12, "bold"), command=known_clicked)
known_button.config(width=8, height=4, bg="#ea4492")
known_button.grid(row=2, column=1)
unknown_button = Button(text="✘", font=("Ariel", 12, "bold"), command=next_card)
unknown_button.config(width=8, height=4, bg="#0561ff")
unknown_button.grid(row=2, column=0)

next_card()

window.mainloop()