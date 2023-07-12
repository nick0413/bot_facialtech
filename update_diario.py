from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import pandas as pd
from datetime import date
from os.path import exists
import funciones as func

today = date.today()

# dd/mm/YY
fecha = today.strftime("%d/%m/%Y")
d1=today.strftime("%m/%d/%Y")

pagina='https://crmfacialtec.com/'
correo='facialteccali@gmail.com'
password='1018472666123'

credenciales=[correo,password]

driver = webdriver.Chrome()
actions = ActionChains(driver)



archivo="Datos.csv"



func.update_file_daily(driver,archivo,fecha,d1,pagina,credenciales)



