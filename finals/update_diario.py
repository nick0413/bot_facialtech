from selenium import webdriver
from datetime import date
import funciones as func

today = date.today()

# dd/mm/YY
fecha = today.strftime("%d/%m/%Y")
d1=today.strftime("%m/%d/%Y")
driver = webdriver.Chrome()
archivo="Historico_facialtech.csv"
pagina='https://crmfacialtec.com/'
correo='facialteccali@gmail.com'
password='1018472666123'
credenciales=[correo,password]


func.update_daily(driver,archivo,fecha,d1,pagina,credenciales)



