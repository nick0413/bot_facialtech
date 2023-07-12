from datetime import date, timedelta
from selenium import webdriver
import funciones as func
import time
 

def crear_historico(start_date,end_date,nombre_archivo):
    # start_date = date(2022,1,1)
    # end_date = date.today()
    delta = end_date - start_date

    dates1=[]
    dates2=[]
    for i in range(delta.days + 1):
        current_date = start_date + timedelta(days=i)
        dates1.append(current_date.strftime("%d/%m/%Y"))
        dates2.append(current_date.strftime("%m/%d/%Y"))

    driver = webdriver.Chrome()
    archivo=nombre_archivo+".csv"
    pagina='https://crmfacialtec.com/'
    correo='facialteccali@gmail.com'
    password='1018472666123'
    credenciales=[correo,password]

    func.update_range(driver,archivo,dates1,dates2,pagina,credenciales)
