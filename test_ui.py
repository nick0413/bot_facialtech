import tkinter as tk 
from tkinter import ttk

def button_func():
    print("boton")
def button_func2():
    print("hi")

window=tk.Tk()

window.title("XD")
window.geometry("1000x500")

label=ttk.Label(master=window, text='xd2')
label.pack()

text_1=tk.Text(master=window)
text_1.pack()

entry=ttk.Entry(master=window)
entry.pack()



label=ttk.Label(master=window, text='xd3')
label.pack()
button=ttk.Button(master=window,text='un boton',command=button_func)
button.pack()

button2=ttk.Button(master=window,text='un boton',command=button_func2)
button2.pack()


window.mainloop()

