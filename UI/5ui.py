import tkinter as tk
from tkinter import ttk

def get_x(event):
    print(f'x={event.x}\ty={event.y}')

window=tk.Tk()
window.title('eventos')
window.geometry('1200x800')

text1=tk.Text(window)
text1.pack()

entry1=ttk.Entry(window)
entry1.pack()

button=ttk.Button(window,text='boton1')
button.pack()


button.bind('<Alt-KeyPress-a>',lambda event: print(event))
window.bind('<Motion>',func=get_x)






window.mainloop()