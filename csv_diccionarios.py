print('\n\n------------Archivos CSV. Lectura en Diccionarios------------')

import csv

comidas = [
    ('Pizza de Muzzarella', 'Salsa de tomate y queso Muzarella', 3200),
    ('Pizza de Jamon y Morrones', 'Salsa de tomate, jamón y morrones', 3500),
    {'Pizza de Fugazzeta', 'Cebolla, Queso Muzzarella y Aceitunas', 3500},
]

with open('clase archivos/comidas_dicc.csv','w', newline='\n') as archivo:
    campos = ['nombre', 'descripcion', 'precio']
    writer = csv.DictWriter(archivo, fieldnames=campos)
    writer.writeheader()
    for nombre, descripcion, precio in comidas:
        writer.writerow({
            'nombre':nombre,
            'descripcion': descripcion,
            'precio': precio
        })

archivo.close()
del (archivo)

print('\n\n-------------Archivos CSV. Escritura en Diccionarios-----------')

import csv

with open('clase archivos/comidas_dicc.csv','r', newline='\n') as archivo:
    reader = csv.DictReader(archivo)
    for cliente in reader:
        print(cliente['nombre'],
              cliente['descripcion'],
              cliente['precio'])