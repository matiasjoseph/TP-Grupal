class Comida:
    def __init__(self, nombre, cantidad, precio):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def generar_dic(self):
        return {'nombre': self.nombre, 'cantidad': self.cantidad, 'precio': self.precio}


    def __str__(self):
        return f'nombre: {self.nombre}\ncantidad: {self.cantidad} \nprecio: {self.precio}'

    def informacion(self):
        return print(self)


def agregar_a_carta(pro, cant, precio):
    cant = int(cant)
    # for a in cocina:
    # if a.nombre == pro and a.cantidad > cant:
    val = precio
    item = Comida(pro, cant, val)
    print(item)
    stock.append(item)
    # a.cantidad -= cant





def hacer_visible(elemento):
    listita = []
    if elemento == 'cocina':
        for prod in cocina:
            listita.append(prod.generar_dic())
        print(listita)
    elif elemento == 'stock':
        for prod in stock:
            listita.append(prod.generar_dic())
        print(listita)


def pagar():
    total = 0
    for i in stock:
        total += i.cantidad * i.precio
    input('\nEn que medio quiere pagar? (Efectivo, Tarjeta de crédito/débito, Transferencia bancaria y PayPal): ')
    print(f'Usted debe pagar {total} pesos')


def salir():
    print('Gracias por utilizar nuestro servicios')

def cambiar_informacion(prod, new):
    j = 0
    for i in stock:

        if stock[j].nombre == prod:
            stock[j].nombre = new
    j = j+1

def eliminar_de_carta(comida):
    for i in stock:
        if i.nombre == comida:
            stock.remove(i)

cocina = []
stock = []

Flag = True

while Flag:

    print('\nBienvenido a la Rotiseria')
    try:

        while Flag:
            print('\nQue accion desea realizar?')
            print('1) Revisar Pedido')
            print('2) Agregar Cosas al Pedido')
            print('3) Eliminar Cosas del Pedido')
            print('4) Cambiar Nombre del Pedido')
            print('5) Pagar')
            print('6) Salir')

            try:
                num = int(input('>> '))

                if num == 1:
                    hacer_visible('stock')
                elif num == 2:
                    agregar_a_carta(input('Nombre del plato: '), int(input('Cantidad: ')), int(input('Precio: ')))
                elif num == 3:
                    eliminar_de_carta (input('Que plato desea eliminar?: '))
                elif num == 4:

                    prod = input('Ingrese el nombre del plato para cambiar:  ')
                    new = input('Ingrese el nombre del nuevo plato:  ')
                    cambiar_informacion(prod, new)

                elif num == 5:
                    pagar()

                elif num == 6:
                    salir()
                    Flag = False
                else:
                    break
            except:
                print("\nDebe ingresar numeros, no letras")


    except:
        print("\nDebe ingresar numeros, no letras")

