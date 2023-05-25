print('\n\nMenu de comidas')

from flask import Flask, jsonify, request

app = Flask(__name__)


menues = [
    {'Nombre': 'tensiometro', 'descripcion: ', 'precio': 5},
    {'Nombre': 'termometro', 'descripcion: ', 'precio': 20},
    {'Nombre': 'ibupofreno', 'descripcion: ', 'precio': 500},
    {'Nombre': 'paracetamol', 'descripcion: ', 'precio': 450},
]

@app.route('/saludo')
def saludo():
    return jsonify({'message': 'Hola!'})


#
#[GET] Consultando información de todos los menues
#
@app.route('/menues', methods=['GET'])
def menuesGet():
    return jsonify({'menues':menues, 'estado':'ok' })

#
# [GET] Consultando información de un único menu
#
@app.route('/menues/<menu>', methods=['GET'])
def menuesGet(menu):
    for indice, p in enumerate(menues):
        if p['Nombre'] == menu:
            return jsonify({'menu':menu[indice], 'busqueda':producto, 'estado':'ok'})
    return jsonify({'productos':productos, 'estado':'no encontrado' })


#
# [POST] Dando de alta un nuevo menu
#
@app.route('/menues', methods=['POST'])
def menuPost():
    body = request.json
    nombre = body['Nombre']
    descripcion = body['descripcion']
    precio  = body['precio']
    menuAlta = {'Nombre': nombre, 'descripcion': descripcion, 'precio': precio}
    productos.append(menuAlta)
    return jsonify({'menues':menues, 'estado':'ok' })

#
# [PUT] Actualiza un Menu
#
@app.route('/menues', methods=['PUT'])
def menuPut():
    body = request.json
    nombre = body['Nombre']
    descripcion = body['descripcion']
    precio  = body['precio']
    for indice, p in enumerate(menues):
        if p['Nombre'] == nombre:
           p['descripcion'] == descripcion:
           p['precio'] = precio
           return jsonify({'menu': p,
                           'busqueda': nombre,
                           'estado': 'ok'})

    return jsonify({'busqueda':menues,
                    'estado':'no encontrado' })



#
# [DELETE] Consultando información de un único producto
#
@app.route('/menues/<menu>', methods=['DELETE'])
def menuDelete(menu):
    for indice, p in enumerate(menues):
        if p['Nombre'] == menu:
            menues[indice:indice+1] = []
            return jsonify({'menu':p, 'busqueda':producto, 'estado':'ok'})
    return jsonify({'menues':menues, 'estado':'no encontrado' })




if __name__ == '__main__':
    app.run(debug=True, port=5000)


