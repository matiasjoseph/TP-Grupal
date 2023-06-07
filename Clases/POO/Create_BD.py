import sqlite3

conexion = sqlite3.connect('base de datos/nueva_Base.db')
conexion.close()

import sqlite3

conexion = sqlite3.connect('base de datos/creo_Base.db')

cursor = conexion.cursor()

sentenciaSQL = 'CREATE TABLE menues'
sentenciaSQL = sentenciaSQL + '(nombre VARCHAR(50),'
sentenciaSQL = sentenciaSQL + ' menues integer)'

cursor.execute(sentenciaSQL)

conexion = sqlite3.connect('base de datos/creo_Base.db')
conexion.close()


import sqlite3

conexion = sqlite3.connect('base de datos/creo_Base.db')

cursor = conexion.cursor()

sentenciaSQL = "INSERT INTO menues "
sentenciaSQL = sentenciaSQL + "VALUES ('Pizza de Mozzarella', 'Salsa de tomate y queso Mozarella', 3200)"
sentenciaSQL = sentenciaSQL + "VALUES ('Pizza de Jamon y Morrones', 'Salsa de tomate, jamón y morrones', 3200)"


cursor.execute(sentenciaSQL)

conexion.commit()
conexion.close()
