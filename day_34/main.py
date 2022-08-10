# Import Modules
from tkinter import messagebox
from tkinter import *
import requests
import random
import html

current_question_number = 0
user_answer = None
current_question = {}
score = 0

# Url and parameters of API
question_api_url = "https://opentdb.com/api.php"
parameters = {
    "amount" : 25,
    "type" : "boolean"
}

# send request to API
response = requests.get(question_api_url, params=parameters)

# edit received data
if response.status_code ==200:
    data = response.json()
    question_data  = data["results"]
    question_bank = []
    for question in question_data:
        question_text = question["question"]
        question_answer = question["correct_answer"]
        new_question = {
            "question_text" : question_text, 
            "question_answer": question_answer
            }
        question_bank.append(new_question)
else:
    print("Error!")

# ---------------------------- DEFINING FUNCTIONS ------------------------------- #

def quiz_still_has_question():
    global current_question_number
    if current_question_number<=24:
        next_question()
    else:
        messagebox.showinfo(title="Game Over", message=f"Your Score is {score}/25")

def next_question():
    global current_question
    global current_question_number
    global score
    current_question = random.choice(question_bank)
    canvas.itemconfig(question_label, text=html.unescape(current_question["question_text"]))
    current_question_number+=1
        
def check_answer():
    global user_answer
    global score
    correct_answer = current_question["question_answer"]
    if user_answer == correct_answer:
        score+=1
    score_label.config(text=f"Score: {score}/{current_question_number}")
    quiz_still_has_question()

def true_button():
    global user_answer
    user_answer = "True"  
    check_answer()

def false_button():
    global user_answer
    user_answer = "False" 
    check_answer()

# ---------------------------- UI SETUP ------------------------------- #

# Window Settings
window = Tk()
window.config(padx=20, pady=20,bg="#D9D7F1")
window.resizable(width=False, height=False)
window.title("Quiz Game")

# Canvas Settings
canvas = Canvas(window,width=460, height=380,highlightthickness=0,bg="#D9D7F1")
canvas.create_oval(10,10, 450,370,fill="#B2A4FF")
canvas.grid(row=1, column=0, columnspan=3)
question_label = canvas.create_text(235, 185, width= 400,text="",font=("Courier", 14, "bold"))
score_label = Label(text="Score: 0/25", font=("Courier", 18, "bold"),bg="#D9D7F1")
score_label.grid(row=0, column=1, columnspan=2)

# Buttons Settings
true_button = Button(text="✔", width=8, height=4, bg="#A26EA1",font=("Ariel", 12, "bold"), command=true_button)
false_button = Button(text="✖",width=8, height=4,bg="#556FB5" ,font=("Ariel", 12, "bold"), command=false_button)
true_button.grid(row=2, column=0)
false_button.grid(row=2, column=1, columnspan=2)

next_question()

window.mainloop()
