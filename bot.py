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


today = date.today()

# dd/mm/YY
fecha = today.strftime("%d/%m/%Y")
d1=today.strftime("%m/%d/%Y")
fecha='12/07/2023'
d1='12/07/2023'
# print("d1 =", d1.replace('/','-'))


pagina='https://crmfacialtec.com/'
correo='facialteccali@gmail.com'
password='1018472666123'

driver = webdriver.Chrome()
actions = ActionChains(driver) 
def get_row(d1,fecha):
	driver.get(pagina)

	WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="usuario"]'))).send_keys(correo)
	WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="clave"]'))).send_keys(password)

	actions.send_keys(Keys.RETURN)
	actions.perform()
	actions.reset_actions()

	WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="estadisticas"]/a/span'))).click()
	WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="fecha_inicio"]'))).send_keys(d1)
	WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="fecha_final"]'))).send_keys(d1)
	WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="frmFechasEstadisticas"]/section[2]/section/button'))).click()

	time.sleep(1)


	ventas=			driver.find_element(By.XPATH,'//*[@id="InformacionDetallada"]/div[1]/label[2]').text
	efectivo=		driver.find_element(By.XPATH,'//*[@id="InformacionDetallada"]/div[3]/label[2]').text
	Datafono=		driver.find_element(By.XPATH,'//*[@id="InformacionDetallada"]/div[4]/label[2]').text
	Transferencia=	driver.find_element(By.XPATH,'//*[@id="InformacionDetallada"]/div[5]/label[2]').text
	Egresos=		driver.find_element(By.XPATH,'//*[@id="InformacionDetallada"]/div[2]/label[2]').text
	Descuentos=		driver.find_element(By.XPATH,'//*[@id="InformacionDetallada"]/div[6]/label[2]').text
	Bancos= 		driver.find_element(By.XPATH,'//*[@id="InformacionDetallada"]/div[7]/label[2]').text
	efectivo_egre= 	driver.find_element(By.XPATH,'//*[@id="InformacionDetallada"]/div[8]/label[2]').text
	T_bancos=		driver.find_element(By.XPATH,'//*[@id="InformacionDetallada"]/div[9]/label[2]').text
	T_efectivo=		driver.find_element(By.XPATH,'//*[@id="InformacionDetallada"]/div[10]/label[2]').text
	Facebook= 		driver.find_element(By.XPATH,'//*[@id="InformacionDetallada"]/div[11]/label[2]').text
	Google=			driver.find_element(By.XPATH,'//*[@id="InformacionDetallada"]/div[12]/label[2]').text
	Pasando=		driver.find_element(By.XPATH,'//*[@id="InformacionDetallada"]/div[13]/label[2]').text
	Instagram=		driver.find_element(By.XPATH,'//*[@id="InformacionDetallada"]/div[14]/label[2]').text
	Recomendado=	driver.find_element(By.XPATH,'//*[@id="InformacionDetallada"]/div[15]/label[2]').text
	Link_agenda=	driver.find_element(By.XPATH,'//*[@id="InformacionDetallada"]/div[16]/label[2]').text
	Sin_fuente=		driver.find_element(By.XPATH,'//*[@id="InformacionDetallada"]/div[17]/label[2]').text
	C_perdidos=		driver.find_element(By.XPATH,'//*[@id="InformacionDetallada"]/div[18]/label[2]').text
	C_recurrentes=	driver.find_element(By.XPATH,'//*[@id="InformacionDetallada"]/div[19]/label[2]').text
	Cumple=			driver.find_element(By.XPATH,'//*[@id="InformacionDetallada"]/div[20]/label[2]').text

	driver.quit()

	#"ventas","efectivo","Datafono","Transferencia","Egresos","Descuentos","Bancos","efectivo_egre","T_bancos","T_efectivo","Facebook","Google","Pasando","Instagram","Recomendado","Link_agenda","Sin_fuente","C_perdidos","C_recurrentes","Cumple"
	labels=['fecha',"ventas","efectivo","Datafono","Transferencia","Egresos","Descuentos","Bancos","efectivo_egre","T_bancos","T_efectivo","Facebook","Google","Pasando","Instagram","Recomendado","Link_agenda","Sin_fuente","C_perdidos","C_recurrentes","Cumple"]
	datos=[fecha,ventas,efectivo,Datafono,Transferencia,Egresos,Descuentos,Bancos,efectivo_egre,T_bancos,T_efectivo,Facebook,Google,Pasando,Instagram,Recomendado,Link_agenda,Sin_fuente,C_perdidos,C_recurrentes,Cumple]


	new_row = pd.Series({
				"fecha":fecha,
				"ventas":ventas,
				"efectivo":efectivo,
				"Datafono":Datafono,
				"Transferencia":Transferencia,
				"Egresos":Egresos,
				"Descuentos":Descuentos,
				"Bancos":Bancos,
				"efectivo_egre":efectivo_egre,
				"T_bancos":T_bancos,
				"T_efectivo":T_efectivo,
				"Facebook":Facebook,
				"Google":Google,
				"Pasando":Pasando,
				"Instagram":Instagram,
				"Recomendado":Recomendado,
				"Link_agenda":Link_agenda,
				"Sin_fuente":Sin_fuente,
				"C_perdidos":C_perdidos,
				"C_recurrentes":C_recurrentes,
				"Cumple":Cumple,
				})
	return new_row,labels

archivo="Datos.csv"
def update_file(archivo):

	new_row,labels=get_row(d1,fecha)
		

	file_exists = exists(archivo)

	if not file_exists:
		df=pd.DataFrame(columns=labels)
		# print(df)

	if file_exists:
		df=pd.read_csv(archivo)





	if	fecha not in df.values :
		print(f"fecha={fecha}")
		df = df.append(new_row, ignore_index=True)
		
	else:
		index=df.index
		index_bool=(df["fecha"] == fecha)
		cumplen=index[index_bool].to_list()
		print(cumplen)
		df.loc[cumplen[0]]=new_row
		print("si esta")





print(df)
df.to_csv(archivo,index=False)






