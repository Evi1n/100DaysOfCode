# Import Modules
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from random import choice, randint, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

def save():
    website = website_entry.get()      
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email" : email,
            "password" : password,
        }
    }
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        try: 
            with open("my_passwords.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("my_passwords.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)
            with open("my_passwords.json", "w") as data_file:
                # Saving new data
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- FIND PASSWORD ------------------------------- #

def search():
    website = website_entry.get()
    try:
        with open("my_passwords.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found!")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exist.")

# ---------------------------- UI SETUP ------------------------------- #

# Window Settings
window = Tk()
window.config(bg="#e1e5f2", padx=20, pady=20)
window.title("MyPass")
window.resizable(width=False, height=False)

# Icon Settings
canvas = Canvas(window, height=250, width=300, bg="#e1e5f2", highlightthickness=0)
img_lock = ImageTk.PhotoImage(Image.open("icon.png"))
canvas.create_image(-10,0,anchor=NW, image=img_lock)
canvas.create_text(90, 210, text="MyPass", fill="#6a00f4", font=("Courier", 30, "bold"))
canvas.grid(row=0, column=1, columnspan=2)

# Label Settings
website_label = Label(window, text="Website", fg="#6a00f4", bg="#e1e5f2", font=("Courier", 12, "bold"), highlightthickness=0)
website_label.grid(row=1, column=0)
username_label = Label(window, text="Email/Username", fg="#6a00f4", bg="#e1e5f2", font=("Courier", 12, "bold"), highlightthickness=0)
username_label.grid(row=2, column=0)
password_label = Label(window, text="Password", fg="#6a00f4", bg="#e1e5f2", font=("Courier", 12, "bold"), highlightthickness=0)
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry(width=31)
website_entry.grid(row=1, column=1)
email_entry = Entry(width=50)
email_entry.grid(row=2, column=1,columnspan=2)
password_entry = Entry(width=31)
password_entry.grid(row=3, column=1)

# Button Settings
search_button = Button(text="Search", width=14, command=search)
search_button.grid(row=1, column=2)
generator_button  = Button(text="Generate Password", command=generate_password)
generator_button.grid(row=3,column=2)
add_button  = Button(text="Add", width=42, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()

