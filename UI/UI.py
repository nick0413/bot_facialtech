

import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar

def select_date():
    selected_date = cal.selection_get()
    # print(selected_date)
    text1.set(selected_date)

text1=tk.StringVar(value='XD')
# Create the main Tkinter window
window = tk.Tk()
window.title("Date Selector")

# Create a Calendar widget
cal = Calendar(window, selectmode="day")

# Create a button to trigger date selection
select_button = ttk.Button(window, text="Select Date", command=select_date)

# Grid layout
cal.grid(row=0, column=0, padx=10, pady=10)
select_button.grid(row=1, column=0, padx=10, pady=10)

# Start the Tkinter event loop
window.mainloop()