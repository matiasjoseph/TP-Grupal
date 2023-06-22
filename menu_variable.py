class Comida:
    def __init__(self, nombre, descripcion, precio):
        self.precio = precio
        self.nombre = nombre
        self.descripcion = descripcion


    def generar_dic(self):
        return {'nombre': self.nombre, 'descripcion': self.descripcion, 'precio': self.precio}

    def cambiar_informacion(self, dato, plato):
        if dato == 'nombre':
            self.nombre = plato

    def __str__(self):
        return f'nombre: {self.nombre}\ndescripcion: {self.descripcion} \nPrecio: {self.precio} pesos'

    def informacion(self):
        return print(self)


def agregar_a_carta(pro, cant, precio):
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

cocina = []

Flag = True

while Flag:
    stock = []
    print('\nBienvenido a la Rotiseria')
    try:

        while Flag:
                print('\nQue accion desea realizar?')
                print('1) Revisar Pedido')
                print('2) Agregar Cosas al Pedido')
                print('3) Eliminar Cosas del Pedido')
                print('4) Cambiar dato del Pedido')
                print('5) Pagar')
                print('6) Salir')

                try:
                    num = int(input('>> '))

                    if num == 1:
                        hacer_visible('cocina')
                    elif num == 2:
                        agregar_a_carta(input('Nombre del plato: '), int(input('Cantidad: ')), int(input('Precio: ')))
                    elif num == 3:
                        eliminar_de_carta(input('Que plato desea eliminar?: '))
                    elif num == 4:
                        prod = input('Ingrese el nombre del plato para cambiar:  ')
                        for i in cocina:
                            if i.nombre == prod:
                                i.cambiar_informacion(input('Que desea cambiar?: '), input('>> '))
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