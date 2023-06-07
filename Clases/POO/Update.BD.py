import sqlite3

conexion = sqlite3.connect('base de datos/MenuesBBDD.db')

cursor = conexion.cursor()

sentenciaSQL  = "UPDATE menues SET stock = stock - 1 WHERE nombre = 'Pizza de Muzzarella'  "
cursor.execute(sentenciaSQL)

sentenciaSQL  = "SELECT * FROM menues  WHERE nombre = 'Pizza de Muzzarella'  "
cursor.execute(sentenciaSQL)

menues = cursor.fetchall()
for menu in menues:
    print("Menu: ", menu)

conexion.close()
