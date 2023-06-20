import pandas as pd

comidas = [
    {
        'Nombre': 'Pizza de Muzzarella',
        'descripcion': 'Salsa de tomate y queso Muzarella',
        'precio': 3200
    },
    {
        'Nombre': 'Pizza de Jamon y Morrones',
        'descripcion': 'Salsa de tomate, jamón y morrones',
        'precio': 3500
    },
    {
        'Nombre': 'Pizza de Fugazzeta',
        'descripcion': 'Cebolla, Queso Muzzarella y Aceitunas',
        'precio': 3500
    },
]

com = pd.DataFrame(comidas)

print(com.describe())