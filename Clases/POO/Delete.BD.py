import sqlite3

conexion = sqlite3.connect('base de datos/MenuesBBDD.db')

cursor = conexion.cursor()

print('\n\n--[Borrar Pizza de Muzzarella]----- ')
sentenciaSQL  = "DELETE FROM menues WHERE nombre = 'Pizza de Muzzarella' "
cursor.execute(sentenciaSQL)


sentenciaSQL  = "SELECT * FROM menues   "
cursor.execute(sentenciaSQL)

menues = cursor.fetchall()
for menu in menues:
    print("Menu: ", menu)

conexion.close()
