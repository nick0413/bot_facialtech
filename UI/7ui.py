from ttkbootstrap import Style
import tkinter as tk
from tkinter import ttk
from datetime import date
import ttkbootstrap as tb
import update_historico

def update_label(*args):
    label_text.set(entry_text.get())

def update_date1():
    
    label_text.set(f'fecha: {date_text.get()}')
root = tk.Tk()
root.title("Entry and Label Example")


style = Style(theme='darkly')

frame = ttk.Frame(root, padding="20")
frame.pack()

entry_text = tk.StringVar()
label_text = tk.StringVar()
date_text=tk.StringVar()

date1=tb.DateEntry(root,bootstyle='warning',dateformat="%d/%m/%Y",startdate=date.today(),firstweekday=0,var=date_text,)
entry = ttk.Entry(frame, textvariable=entry_text)
label = ttk.Label(frame, textvariable=label_text)

date1.pack(pady=10)
# entry.pack(pady=10)
label.pack(pady=10)
date_text.trace_add('write',update_date1)
entry_text.trace_add('write', update_label)

root.mainloop()