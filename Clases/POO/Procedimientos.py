from flask import Flask, jsonify, request

from mod.persona import Persona

app = Flask(__name__)

s = [
    {'Nombre': 'tensiometro', 'descripcion': ', 'precio': 5},
    {'Nombre': 'termometro', 'descripcion': ', 'precio': 20},
    {'Nombre': 'ibupofreno', 'descripcion': ', 'precio': 500},
    {'Nombre': 'paracetamol', 'descripcion': ', 'precio': 450},
]


@app.route('/')
def home():
    return 'Hola!'


@app.route('/saludar/<nombre>/<edad>', methods=['GET'])
def saludar(nombre, edad):
    my_persona = Persona(nombre, edad)
    return 'Hola ' + str(my_persona) + ' !'

@app.route('/menues', methods=['GET'])
def menuesGet():
    return jsonify({'menues':menues, 'estado':'ok' })


@app.route('/menues/<nombre>', methods=['GET'])
def menuesConseguirMenu(nombre):
    for indice, p in enumerate(menues):
        print('p: ', p)
        print('nombre:', nombre)
        if p['Nombre'] == nombre:
            return jsonify({'menues':menues[indice], 'estado':'ok' })
    return 'Error. No se puede obtener el menu'


@app.route('/menues', methods=['POST'])
def menuesPost():
    body = request.json
    print(body)
    nombre = body['Nombre']
    descripcion = body['descripcion']
    precio = body['precio']

    altaMenu = {'Nombre': nombre, 'descripcion': descripcion, 'precio': precio}
    menues.append(altaMenu)

    return jsonify({'menu':menues, 'status':'ok' })




@app.route('/menues', methods=['PUT'])
def menuPutUpdatePorBody():

    body = request.json
    nombre = body['Nombre']
    descripcion = body['descripcion']
    precio = body['precio']

    for indice, p in enumerate(menues):
        if p['Nombre'] == nombre:
            p['descripcion'] = descripcion:
            p['precio'] = precio
    return jsonify({'menues': menues, 'estado': 'ok'})


@app.route('/menues/<nombre>', methods=['DELETE'])
def menuDelete(nombre):
    for indice, p in enumerate(menues):
        if p['Nombre'] == nombre:
            menu[indice: indice+1] = []
    return jsonify({'menues': menues, 'estado': 'ok'})



if __name__ == '__main__':
    app.run(debug=True, port=5000)
