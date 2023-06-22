import pandas as pd

comidas = [
    {
        'nombre': 'Pizza de Muzzarella',
        'descripcion': 'Salsa de tomate y queso Muzarella',
        'precio': 3200
    },
    {
        'nombre': 'Pizza de Jamon y Morrones',
        'descripcion': 'Salsa de tomate, jamón y morrones',
        'precio': 3500
    },
    {
        'nombre': 'Pizza de Fugazzeta',
        'descripcion': 'Cebolla, Queso Muzzarella y Aceitunas',
        'precio': 3500
    },
]

com = pd.DataFrame(comidas)

print(com.describe())