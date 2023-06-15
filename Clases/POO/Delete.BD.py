# SELECT - Todos los Registros
import sqlite3

conexion = sqlite3.connect('base de datos/MenuesBBDD.db')

cursor = conexion.cursor()

sentenciaSQL  = "SELECT * FROM menues "
cursor.execute(sentenciaSQL)

articulos = cursor.fetchall()
for menu in menues:
    print("Menu: ", menu)

conexion.close()


#---------------------------------------------------
# DELETE

import sqlite3

conexion = sqlite3.connect('base de datos/MenuesBBDD.db')

cursor = conexion.cursor()


sentenciaSQL  = "DELETE FROM menues WHERE Nombre = 'Pizza de Muzzarella' "
cursor.execute(sentenciaSQL)


sentenciaSQL  = "SELECT * FROM menues   "
cursor.execute(sentenciaSQL)

menues = cursor.fetchall()
for menu in menues:
    print("Menu: ", menu)

conexion.close()