import tkinter as tk 
import ttkbootstrap as tb
from datetime import date, timedelta
from datetime import datetime
from ttkbootstrap import Style
import time
import update_historico as uh

# Create an instance of the Style class

d1=''
d2=''

def check_dates(date1,date2):

    # datetime_str = '13/08/2200'
    # print(datetime_str,date1)
    datetime1 = datetime.strptime(date1, "%d/%m/%Y").date()
    datetime2 = datetime.strptime(date2, "%d/%m/%Y").date()


    if datetime1==datetime2:
        label_text1.set(f'Error: {date1} es igual a {date2}')

    if datetime2>datetime1:

        delta = datetime2 - datetime1

        label_text2.set(f'Buscando {delta.days} dias')

        # time.sleep(2)

        window.destroy()

        uh.crear_historico(datetime1,datetime2,"datos_prueba")




    if datetime2<datetime1:
        print(f"{datetime2} antes de {datetime1}")
        label_text1.set(f'Error: {date1} va antes de  {date2}')





def get_dates():
    # print('xboton')
    d1=date1.entry.get()
    d2=date2.entry.get()
    label_text1.set(f'Buscando desde {d1} hasta {d2}')
    check_dates(d1,d2)




window= tb.Window(themename="darkly")

window.title("Creador de registro")
window.geometry('700x700')


fecha1=tk.StringVar()
fecha2=tk.StringVar()

label_text1=tk.StringVar()
label_text2=tk.StringVar()

date1=tb.DateEntry(window,bootstyle='warning',dateformat="%d/%m/%Y",startdate=date.today(),firstweekday=0)
date2=tb.DateEntry(window,bootstyle='warning',dateformat="%d/%m/%Y",startdate=date.today(),firstweekday=0)
boton1=tb.Button(window,text='Buscar fechas',bootstyle='warining',command=get_dates)


label1=tb.Label(window,text=f'desde {d1} hasta {d2}',textvariable=label_text1,bootstyle='warning',font=('Arial',16))

label2=tb.Label(window,text='Desde:')
label3=tb.Label(window,text='Hasta:')

label4=tb.Label(window,text='',textvariable=label_text2,bootstyle='warning',font=('Arial',16))


label2.pack()
date1.pack()
label3.pack()
date2.pack()
label1.pack()
boton1.pack()
label4.pack()





window.mainloop()
