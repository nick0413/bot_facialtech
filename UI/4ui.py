import tkinter as tk
from tkinter import ttk

window=tk.Tk()
window.title('botones')
window.geometry('1200x800')


# text1=tk.StringVar(value='boton2')

# def but_func():
#     print('funcion')

# button =ttk.Button(window,text='boton1',command=but_func,textvariable=text1)
# button.pack()


# check_var=tk.BooleanVar()
# check=ttk.Checkbutton(window,text='check1',command=lambda:print(check_var.get()),variable=check_var)
# check.pack()


# radio=tk.StringVar()

# radio1=ttk.Radiobutton(window,text='Radiobutton1',value=1,variable=radio, command= lambda: print(radio.get()))
# radio2=ttk.Radiobutton(window,text='Radiobutton2',value=2,variable=radio, command= lambda: print(radio.get()))
# radio3=ttk.Radiobutton(window,text='Radiobutton3',value=3,variable=radio, command= lambda: print(radio.get()))
# radio1.pack()
# radio2.pack()
# radio3.pack()


radio=tk.StringVar(value='A')
check_var=tk.BooleanVar(value=False)
check=ttk.Checkbutton(window,text='check1',command=lambda:print(radio.get()),variable=check_var)
check.pack()

def f1():
    print(check_var.get())
    check_var.set(False)

radio1=ttk.Radiobutton(window,text='Radiobutton1',value='A',variable=radio, command= f1)
radio2=ttk.Radiobutton(window,text='Radiobutton2',value='B',variable=radio, command= lambda: print(check_var.get()))
radio1.pack()
radio2.pack()

window.mainloop()



