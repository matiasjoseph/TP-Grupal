import sqlite3

conexion = sqlite3.connect('base de datos/MenuesBBDD.db')

try:
    cursor = conexion.cursor()
    sentenciaSQL = 'CREATE TABLE menues'
    sentenciaSQL = sentenciaSQL + '(nombre VARCHAR(100),'
    sentenciaSQL = sentenciaSQL + ' stock integer)'
    cursor.execute(sentenciaSQL)

except Exception as e:
    print('Hubo una Exception: ', e)

conexion = sqlite3.connect('base de datos/MenuesBBDD.db')
conexion.close()

import sqlite3

conexion = sqlite3.connect('base de datos/MenuesBBDD.db')

cursor = conexion.cursor()


sentenciaSQL  = "INSERT INTO menues "
sentenciaSQL += "VALUES ('Pizza de Mozzarella', 'salsa de tomate y queso mozzarella', 3200)"
cursor.execute(sentenciaSQL)

sentenciaSQL  = "INSERT INTO menues "
sentenciaSQL += "VALUES ('Pizza de Jamon y Morrones', 'salsa de tomate, jamon y morrones', 3500)"
cursor.execute(sentenciaSQL)

sentenciaSQL  = "INSERT INTO menues "
sentenciaSQL += "VALUES ('Pizza de Fugazzeta', 'Cebolla, queso mozzarella y aceitunas', 3500)"
cursor.execute(sentenciaSQL)

cursor.execute(sentenciaSQL)

conexion.commit()
conexion.close()


import sqlite3

conexion = sqlite3.connect('base de datos/MenuesBBDD.db')

cursor = conexion.cursor()

menues = [
    ('Pizza Napolitana', 'salsa de tomate, queso mozzarella, rodajas de tomates y aceitunas', 3200),
    ('Empanada de Carne',  'Relleno de Carne Picada, Cebolla y Aceitunas', 300),
    ('Empanada de Pollo ',  'Relleno de Pollo Desmenuzado, Cebolla y Queso Mozzarella', 300)
]

sentenciaSQL = "INSERT INTO menues VALUES (?, ?)"
cursor.executemany(sentenciaSQL, menues)

conexion.commit()
conexion.close()