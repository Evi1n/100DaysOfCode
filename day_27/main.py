from tkinter import *

# Calculate to km
def miles_to_km():
    miles = float(miles_input.get())
    km = miles * 1.609
    km_result_label.config(text=f"{km}")

# Window Settings
window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=200, height=120)
window.config(padx=12, pady=20)

# Miles Input Settings (entry)
miles_input = Entry()
miles_input.grid(column=1, row=0)
miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

# Labels
equal_label = Label(text="is equal to")
equal_label.grid(column=0, row=1)

km_result_label = Label(text="0")
km_result_label.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

# Calculate Button Settings
calculate_button = Button(text="Calculate", command=miles_to_km)
calculate_button.grid(column=1, row=2)

window.mainloop()