# UNIDAD 09.D50 Bases de Datos
# SQL. Visualizando y administrando una base de datos


#---------------------------------------------------
# Base de Dato Vacia
import sqlite3

conexion = sqlite3.connect('base de datos/nueva_Base.db')
conexion.close()


#---------------------------------------------------
# Creando una Tabla desde Python
import sqlite3

conexion = sqlite3.connect('base de datos/creo_Base.db')

cursor = conexion.cursor()

sentenciaSQL = 'CREATE TABLE menues'
sentenciaSQL = sentenciaSQL + '(nombre VARCHAR(50),'
sentenciaSQL = sentenciaSQL + ' menues integer)'

cursor.execute(sentenciaSQL)

conexion = sqlite3.connect('base de datos/creo_Base.db')
conexion.close()


#---------------------------------------------------
# Insertando registros en la tabla
import sqlite3

conexion = sqlite3.connect('base de datos/creo_Base.db')

cursor = conexion.cursor()

sentenciaSQL = "INSERT INTO menues "
sentenciaSQL = sentenciaSQL + "VALUES ('Pizza de Muzzarella', 'Salsa de tomate y queso Muzarella', 3200)"
sentenciaSQL = sentenciaSQL + "VALUES ('Pizza de Jamon y Morrones', 'Salsa de tomate, jamón y morrones', 3200)"


cursor.execute(sentenciaSQL)

conexion.commit()
conexion.close()
