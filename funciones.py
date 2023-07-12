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

labels=['fecha',"ventas","efectivo","Datafono","Transferencia","Egresos","Descuentos","Bancos","efectivo_egre","T_bancos","T_efectivo","Facebook","Google","Pasando","Instagram","Recomendado","Link_agenda","Sin_fuente","C_perdidos","C_recurrentes","Cumple"]

def get_data(driver,d1,fecha):

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
	C_perdidos=		driver.find_element(By.XPATH,'//*[@id="InformacionDetallada"]/div[18]/label[2]').text.replace('Cantidad:','')
	C_recurrentes=	driver.find_element(By.XPATH,'//*[@id="InformacionDetallada"]/div[19]/label[2]').text.replace('Cantidad:','')
	Cumple=			driver.find_element(By.XPATH,'//*[@id="InformacionDetallada"]/div[20]/label[2]').text

	

	#"ventas","efectivo","Datafono","Transferencia","Egresos","Descuentos","Bancos","efectivo_egre","T_bancos","T_efectivo","Facebook","Google","Pasando","Instagram","Recomendado","Link_agenda","Sin_fuente","C_perdidos","C_recurrentes","Cumple"

	datos=[fecha,ventas,efectivo,Datafono,Transferencia,Egresos,Descuentos,Bancos,efectivo_egre,T_bancos,T_efectivo,Facebook,Google,Pasando,Instagram,Recomendado,Link_agenda,Sin_fuente,C_perdidos,C_recurrentes,Cumple]

	return datos

def panda_series(columns,datos):
	new_row = pd.DataFrame({
				columns[0]:[datos[0]],
				columns[1]:[datos[1]],
				columns[2]:[datos[2]],
				columns[3]:[datos[3]],
				columns[4]:[datos[4]],
				columns[5]:[datos[5]],
				columns[6]:[datos[6]],
				columns[7]:[datos[7]],
				columns[8]:[datos[8]],
				columns[9]:[datos[9]],
				columns[10]:[datos[10]],
				columns[11]:[datos[11]],
				columns[12]:[datos[12]],
				columns[13]:[datos[13]],
				columns[14]:[datos[14]],
				columns[15]:[datos[15]],
				columns[16]:[datos[16]],
				columns[17]:[datos[17]],
				columns[18]:[datos[18]],
				columns[19]:[datos[19]],
				columns[20]:[datos[20]]
				})
	return new_row

def get_row(driver,pagina,d1,credenciales,fecha):
	correo=credenciales[0]
	password=credenciales[1]
	driver.get(pagina)
	actions = ActionChains(driver)

	WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="usuario"]'))).send_keys(correo)
	WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="clave"]'))).send_keys(password)

	actions.send_keys(Keys.RETURN)
	actions.perform()
	actions.reset_actions()

	WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="estadisticas"]/a/span'))).click()


	datos=get_data(driver,d1,fecha)

	new_row = panda_series(labels,datos)
	return new_row




def update_file_daily(driver,archivo,fecha,d1,pagina,credenciales):

	new_row=get_row(driver,pagina,d1,credenciales,fecha)
	driver.quit()
	df=pd.DataFrame(columns=labels)
    
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
		print(f"actualizando fila{cumplen}")
		df.loc[cumplen[0]]=new_row
		print(df)
		df.to_csv(archivo,index=False)

def access_page(driver,credenciales):
	correo=credenciales[0]
	password=credenciales[1]
	actions = ActionChains(driver)

	WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="usuario"]'))).send_keys(correo)
	WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="clave"]'))).send_keys(password)

	actions.send_keys(Keys.RETURN)
	actions.perform()
	actions.reset_actions()

	WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="estadisticas"]/a/span'))).click()

def fill_and_search(driver,d1):

	WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="fecha_inicio"]'))).send_keys(d1)
	WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="fecha_final"]'))).send_keys(d1)
	WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="frmFechasEstadisticas"]/section[2]/section/button'))).click()

def get_datos(driver,fecha):
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
	C_perdidos=		driver.find_element(By.XPATH,'//*[@id="InformacionDetallada"]/div[18]/label[2]').text.replace('Cantidad:','')
	C_recurrentes=	driver.find_element(By.XPATH,'//*[@id="InformacionDetallada"]/div[19]/label[2]').text.replace('Cantidad:','')
	Cumple=			driver.find_element(By.XPATH,'//*[@id="InformacionDetallada"]/div[20]/label[2]').text

	

	#"ventas","efectivo","Datafono","Transferencia","Egresos","Descuentos","Bancos","efectivo_egre","T_bancos","T_efectivo","Facebook","Google","Pasando","Instagram","Recomendado","Link_agenda","Sin_fuente","C_perdidos","C_recurrentes","Cumple"

	datos=[fecha,ventas,efectivo,Datafono,Transferencia,Egresos,Descuentos,Bancos,efectivo_egre,T_bancos,T_efectivo,Facebook,Google,Pasando,Instagram,Recomendado,Link_agenda,Sin_fuente,C_perdidos,C_recurrentes,Cumple]

	return datos

def update_range(driver,archivo,fechas,ds,pagina,credenciales):
	
	if len(fechas)!=len(ds): 
		raise Exception("las fechas en formato no son iguales")

    
	file_exists = exists(archivo)

	if not file_exists:
		df=pd.DataFrame(columns=labels)
		# print(df)
 
	else:
		df=pd.read_csv(archivo)

	driver.get(pagina)
	access_page(driver,credenciales)
	print(ds)
	print(fechas)

	for i in range(len(fechas)):
		fill_and_search(driver,ds[i])
		datos=get_datos(driver,fechas[i])
		new_row=panda_series(labels,datos)
		# print(new_row)
			
		if	fechas[i] not in df.values :
			print(f"fecha={fechas[i]}")
			df=pd.concat([new_row,df.loc[:]],sort=False).reset_index(drop=True)
		
		else:

			# ind=df.loc[df["fecha"]==fechas[i]]
			# df.loc[ind]=new_row
			print(f"fecha={fechas[i]}")
			index = df.loc[df['fecha'] == fechas[i]].index
			df.loc[index] = new_row
			# index=df.index
			# index_bool=(df["fecha"] == fechas[i])
			# cumplen=index[index_bool].to_list()
			# df.loc[cumplen[0]]=new_row


		time.sleep(0.5)

	df.to_csv(archivo,index=False)

	driver.quit()
		
