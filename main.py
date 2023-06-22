
print('\n\nMenu de comidas')

from flask import Flask, jsonify, request
from crear_tabla import create_tables, seed_comidas
from Usuario import Persona

app = Flask(__name__)

menues = [
    {'nombre': 'Pizza de Muzzarella', 'descripcion': 'Salsa de tomate y queso Muzarella', 'precio': 3200},
    {'nombre': 'Pizza de Jamon y Morrones', 'descripcion': 'Salsa de tomate, jamón y morrones', 'precio': 3500},
    {'nombre': 'Pizza de Fugazzeta', 'descripcion': 'Cebolla, Queso Muzzarella y Aceitunas', 'precio': 3500},
    {'nombre': 'Pizza Napolitana', 'descripcion': 'Salsa de tomate, Queso Mozzarella, Rodajas de Tomates y Aceitunas', 'precio': 3200},
    {'nombre': 'Empanada de Carne', 'descripcion': 'Relleno de Carne Picada, Cebolla y Aceitunas','precio': 300},
    {'nombre': 'Empanada de Pollo', 'descripcion': 'Relleno de Pollo Desmenuzado, Cebolla y Queso Muzarella','precio': 300},
    {'nombre': 'Empanada de Jamon y Queso', 'descripcion': 'Relleno de Jamon Cocido y Queso Muzarella','precio': 300},
    {'nombre': 'Empanada de Verduras', 'descripcion': 'Relleno de Espinaca, Acelga y Brocoli con Queso','precio': 300},
    {'nombre': 'Empanada de Humita', 'descripcion': 'Relleno de Choclo, Cebolla y Queso Muzarella', 'precio': 300},
    {'nombre': 'Empanada de Queso y Cebolla', 'descripcion': 'Relleno de Cebolla Caramelizada y Queso Muzarella', 'precio': 300},
    {'nombre': 'Milanesa Simple', 'descripcion': 'Milanesa de Carne o Pollo', 'precio': 2200},
    {'nombre': 'Milanesa a la Napolitana', 'descripcion': 'Milanesa de carne o pollo con salsa de tomate y queso mozzarella.', 'precio': 2900},
    {'nombre': 'Tallarines con salsa boloñesa', 'descripcion': 'Tallarines al dente servidos de salsa bolognesa. Con una salsa preparada con carne molida, tomates, cebolla y especias', 'precio': 1800},
    {'nombre': 'Ñoquis de papa con salsa rosa', 'descripcion': 'Ñoquis caseros de papa acompañados de una salsa mezcla de tomate y salsa blanca.', 'precio': 1800},
    {'nombre': 'Sorrentinos de jamón y queso con salsa cuatro quesos', 'descripcion': 'Sorrentinos rellenos de jamón y queso. La salsa es elaborada con una combinación de quesos como mozzarella, roquefort, parmesano y crema.', 'precio': 2500},
    {'nombre': 'Coca-Cola (lata)', 'precio': 600},
    {'nombre': 'Sprite (lata)', 'precio': 600},
    {'nombre': 'Fanta (lata)', 'precio': 600},
    {'nombre': 'Agua mineral sin gas 500ml','precio': 500},
    {'nombre': 'Agua con gas 500ml', 'precio': 500},
    {'nombre': 'Quilmes 476ml', 'precio': 350},
    {'nombre': 'Patagonia Amber Lager 473ml', 'precio': 550},
    {'nombre': 'Heineken 710ml', 'precio': 700},
    {'nombre': 'Limonada', 'precio': 1000},
    {'nombre': 'Jugo de naranja natural', 'precio': 1000},
    {'nombre': 'Flan casero', 'descripcion': 'Flan casero acompañado con crema y dulce de leche', 'precio': 1100},
    {'nombre': 'Ensalada de fruta', 'descripcion': 'Ensalada de Frutilla, Manzana, Banana, Kiwi y Naranja', 'precio': 850},
    {'nombre': 'Brownie con helado', 'descripcion': 'Brownie casero acompañado con una bocha de helado de dulce de leche o americana', 'precio': 1100},
    {'nombre': 'Fruta a elección', 'descripcion': 'Elección de fruta entre Banana, Manzana, Pera, Kiwi y Durazno', 'precio': 200},
]


@app.route('/')
def home():
    return 'Hola!'



@app.route('/saludar/<nombre>/<edad>', methods=['GET'])
def saludar(nombre, edad):
    my_persona = (nombre, edad)
    return 'Hola ' + nombre + ' , ' +  ' Edad: ' + edad



@app.route('/menues', methods=['GET'])
def menuesGet():
    return jsonify({'menues':menues, 'estado':'ok' })


@app.route('/menues/<nombre>', methods=['GET'])
def menuesConseguirMenu(nombre):
    for indice, p in enumerate(menues):
        print('p: ', p)
        print('nombre:', nombre)
        if p['nombre'] == nombre:
            return jsonify({'menues':menues[indice], 'estado':'ok' })
    return 'Error. No se puede obtener el menu'


@app.route('/menues', methods=['POST'])
def menuesPost():
    body = request.json
    print(body)
    nombre = body['nombre']
    descripcion = body['descripcion']
    precio = body['precio']

    altaMenu = {'nombre': nombre, 'descripcion': descripcion, 'precio': precio}
    menues.append(altaMenu)

    return jsonify({'menu':menues, 'status':'ok' })



@app.route('/menues', methods=['PUT'])
def menuPutUpdatePorBody():

    body = request.json
    nombre = body['nombre']
    descripcion = body['descripcion']
    precio = body['precio']

    for indice, p in enumerate(menues):
        if p['nombre'] == nombre:
            p['descripcion'] = descripcion
            p['precio'] = precio
    return jsonify({'menues': menues, 'estado': 'ok'})


@app.route('/menues/<nombre>', methods=['DELETE'])
def menuDelete(nombre):
    for indice, p in enumerate(menues):
        if p['nombre'] == nombre:
            menues[indice: indice+1] = []
    return jsonify({'menues': menues, 'estado': 'ok'})

create_tables()
seed_comidas()
app.run()


if __name__ == '__main__':
    app.run()




