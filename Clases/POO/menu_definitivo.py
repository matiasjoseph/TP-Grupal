class Comida:
    def __init__(self, Nombre, descripcion, precio):
        self.precio = precio
        self.nombre = nombre
        self.descripcion = descripcion

    def generar_dic(self):
        return {'Nombre': self.nombre, 'descripcion': self.descripcion, 'precio': self.precio}

    def cambiar_informacion(self, dato, cant):
        if dato == 'precio':
            self.precio = cant

    def __str__(self):
        return f'Nombre: {self.nombre}\ndescripcion: {self.descripcion} \nPrecio: {self.precio} pesos'

    def informacion(self):
        return print(self)


# Funciones


def agregar_a_carta(pro, cant):
    cant = int(cant)
    for a in cocina:
        if a.nombre == pro and a.cantidad > cant:
            val = a.precio
            item = Comida(pro, cant, val)
            stock.append(item)
            a.cantidad -= cant


def eliminar_de_carta(comida):
    for i in stock:
        if i.nombre == comida:
            cocina.remove(i)


def pagar():
    total = 0
    for i in stock:
        total += i.cantidad * i.precio
    print(f'Usted debe pagar {total} pesos')


def hacer_visible(elemento):
    listita = []
    if elemento == 'cocina':
        for prod in cocina:
            listita.append(prod.generar_dic())
        print(listita)
    elif cosa == 'stock':
        for prod in stock:
            listita.append(prod.generar_dic())
        print(listita)

def salir():
    print('Gracias por utilizar nuestro servicios')

# Cuerpo

cocina = []


while True:
    stock = []
    print('\nBienvenido a la Rotiseria')
    try:
            while True:
                print('\nQue accion desea realizar')
                print('1) Revisar stock')
                print('2) Agregar a la carta')
                print('3) Eliminar de la carta')
                print('4) Cambiar dato de comida')
                print('5) Salir')

                try:
                    num = int(input('>> '))

                    if num == 1:
                        hacer_visible('cocina')
                    elif num == 2:
                        agregar_a_carta(input('Nombre '), input('Cantidad '))
                    elif num == 3:
                        hacer_visible('stock')
                    elif num == 4:
                        eliminar_de_carta(input('Producto '))
                    elif num == 5:
                        salir()
                        break
                    else:
                        break
                except:
                    print("\nDebe ingresar numeros, no letras")


    except:
        print("\nDebe ingresar numeros, no letras")