import tkinter as tk
from tkinter import ttk

def func1():
    text1.set('no mms')

window=tk.Tk()
window.title('variables')

text1=tk.StringVar(value='XD')



label=ttk.Label(master=window,text="label1",textvariable=text1)
label.pack()



entry=ttk.Entry(master=window,textvariable=text1)
entry.pack()

button=ttk.Button(master=window,text='boton',command=func1)
button.pack()

window.mainloop()