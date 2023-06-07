import sqlite3

conexion = sqlite3.connect('base de datos/FarmaciaBBDD.db')

cursor = conexion.cursor()

sentenciaSQL  = "SELECT * FROM menues   "
cursor.execute(sentenciaSQL)

menues = cursor.fetchall()
for menu in menues:
    print("Menu: ", menues)

conexion.close()
