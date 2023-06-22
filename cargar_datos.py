print('\n\n-------Pickle Graba-------')

import pickle
archivo = open('clase archivos/pickles.pkl','wb')

opcion =  {'nombre': 'Pizza de Muzzarella', 'descripcion': 'Salsa de tomate y queso Muzarella', 'precio': 3200}
pickle.dump(opcion, archivo)

opcion = {'nombre': 'Pizza de Jamon y Morrones', 'descripcion': 'Salsa de tomate, jamón y morrones', 'precio': 3500}
pickle.dump(opcion, archivo)

opcion = {'nombre': 'Pizza de Fugazzeta', 'descripcion': 'Cebolla, Queso Muzzarella y Aceitunas', 'precio': 3500}
pickle.dump(opcion, archivo)

opcion =  {'nombre': 'Pizza Napolitana', 'descripcion': 'Salsa de tomate, Queso Mozzarella, Rodajas de Tomates y Aceitunas', 'precio': 3200}
pickle.dump(opcion, archivo)

opcion =  {'nombre': 'Empanada de Carne', 'descripcion': 'Relleno de Carne Picada, Cebolla y Aceitunas','precio': 300}
pickle.dump(opcion, archivo)

opcion =  {'nombre': 'Empanada de Pollo', 'descripcion': 'Relleno de Pollo Desmenuzado, Cebolla y Queso Muzarella','precio': 300}
pickle.dump(opcion, archivo)

opcion = {'nombre': 'Empanada de Jamon y Queso', 'descripcion': 'Relleno de Jamon Cocido y Queso Muzarella','precio': 300}
pickle.dump(opcion, archivo)

opcion = {'nombre': 'Empanada de Verduras', 'descripcion': 'Relleno de Espinaca, Acelga y Brocoli con Queso','precio': 300}
pickle.dump(opcion, archivo)

opcion = {'nombre': 'Empanada de Humita', 'descripcion': 'Relleno de Choclo, Cebolla y Queso Muzarella', 'precio': 300}
pickle.dump(opcion, archivo)

opcion = {'nombre': 'Empanada de Queso y Cebolla', 'descripcion': 'Relleno de Cebolla Caramelizada y Queso Muzarella', 'precio': 300}
pickle.dump(opcion, archivo)

opcion = {'nombre': 'Milanesa Simple', 'descripcion': 'Milanesa de Carne o Pollo', 'precio': 2200}
pickle.dump(opcion, archivo)

opcion = {'nombre': 'Milanesa a la Napolitana', 'descripcion': 'Milanesa de carne o pollo con salsa de tomate y queso mozzarella.', 'precio': 2900}
pickle.dump(opcion, archivo)

opcion = {'nombre': 'Tallarines con salsa boloñesa', 'descripcion': 'Tallarines al dente servidos de salsa bolognesa. Con una salsa preparada con carne molida, tomates, cebolla y especias', 'precio': 1800}
pickle.dump(opcion, archivo)

opcion = {'nombre': 'Ñoquis de papa con salsa rosa', 'descripcion': 'Ñoquis caseros de papa acompañados de una salsa mezcla de tomate y salsa blanca.', 'precio': 1800}
pickle.dump(opcion, archivo)

opcion = {'nombre': 'Sorrentinos de jamón y queso con salsa cuatro quesos', 'descripcion': 'Sorrentinos rellenos de jamón y queso. La salsa es elaborada con una combinación de quesos como mozzarella, roquefort, parmesano y crema.', 'precio': 2500}
pickle.dump(opcion, archivo)

opcion = {'nombre': 'Coca-Cola (lata)', 'precio': 600}
pickle.dump(opcion, archivo)

opcion = {'nombre': 'Sprite (lata)', 'precio': 600}
pickle.dump(opcion, archivo)

opcion = {'nombre': 'Fanta (lata)', 'precio': 600}
pickle.dump(opcion, archivo)

opcion = {'nombre': 'Agua mineral sin gas 500ml','precio': 500}
pickle.dump(opcion, archivo)

opcion = {'nombre': 'Agua con gas 500ml', 'precio': 500}
pickle.dump(opcion, archivo)

opcion = {'nombre': 'Quilmes 476ml', 'precio': 350}
pickle.dump(opcion, archivo)

opcion = {'nombre': 'Patagonia Amber Lager 473ml', 'precio': 550}
pickle.dump(opcion, archivo)

opcion = {'nombre': 'Heineken 710ml', 'precio': 700}
pickle.dump(opcion, archivo)

opcion = {'nombre': 'Limonada', 'precio': 1000}
pickle.dump(opcion, archivo)

opcion = {'nombre': 'Jugo de naranja natural', 'precio': 1000}
pickle.dump(opcion, archivo)

opcion = {'nombre': 'Flan casero', 'descripcion': 'Flan casero acompañado con crema y dulce de leche', 'precio': 1100}
pickle.dump(opcion, archivo)

opcion = {'nombre': 'Ensalada de fruta', 'descripcion': 'Ensalada de Frutilla, Manzana, Banana, Kiwi y Naranja', 'precio': 850}
pickle.dump(opcion, archivo)

opcion = {'nombre': 'Brownie con helado', 'descripcion': 'Brownie casero acompañado con una bocha de helado de dulce de leche o americana', 'precio': 1100}
pickle.dump(opcion, archivo)

opcion = {'nombre': 'Fruta a elección', 'descripcion': 'Elección de fruta entre Banana, Manzana, Pera, Kiwi y Durazno', 'precio': 200}
pickle.dump(opcion, archivo)


archivo.close()
del archivo

print('\n\n-------Pickle Recupera-------')

import pickle
archivo = open('clase archivos/pickles.pkl','rb')

opcion1 = pickle.load(archivo)
opcion2 = pickle.load(archivo)
opcion3 = pickle.load(archivo)
opcion4 = pickle.load(archivo)
opcion5 = pickle.load(archivo)
opcion6 = pickle.load(archivo)
opcion7 = pickle.load(archivo)
opcion8 = pickle.load(archivo)
opcion9 = pickle.load(archivo)
opcion10 = pickle.load(archivo)
opcion11 = pickle.load(archivo)
opcion12 = pickle.load(archivo)
opcion13 = pickle.load(archivo)
opcion14 = pickle.load(archivo)
opcion15 = pickle.load(archivo)
opcion16 = pickle.load(archivo)
opcion17 = pickle.load(archivo)
opcion18 = pickle.load(archivo)
opcion19 = pickle.load(archivo)
opcion20 = pickle.load(archivo)
opcion21 = pickle.load(archivo)
opcion22 = pickle.load(archivo)
opcion23 = pickle.load(archivo)
opcion24 = pickle.load(archivo)
opcion25 = pickle.load(archivo)
opcion26 = pickle.load(archivo)
opcion27 = pickle.load(archivo)
opcion28 = pickle.load(archivo)
opcion29 = pickle.load(archivo)
print(opcion1)
print(opcion2)
print(opcion3)
print(opcion4)
print(opcion5)
print(opcion6)
print(opcion7)
print(opcion8)
print(opcion9)
print(opcion10)
print(opcion11)
print(opcion12)
print(opcion13)
print(opcion14)
print(opcion15)
print(opcion16)
print(opcion17)
print(opcion18)
print(opcion19)
print(opcion20)
print(opcion21)
print(opcion22)
print(opcion23)
print(opcion24)
print(opcion25)
print(opcion26)
print(opcion27)
print(opcion28)
print(opcion29)

archivo.close()
del (archivo)


               
