import tkinter as tk
from tkinter import ttk

def button_func():
    print(entry.get())

def change_label():
    label.config(text=entry.get())


    
window=tk.Tk()
window.title('getting an setting widgets')


label=ttk.Label(master=window,text='label1')
label.pack()

entry=ttk.Entry(master=window)
entry.pack()

button1=ttk.Button(master=window,text='boton1',command=change_label)
button1.pack()

window.mainloop()

