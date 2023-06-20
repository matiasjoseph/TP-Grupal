class Empleado:
    def __init__(self, nombre, clave):
        self.nombre = nombre
        self.clave = clave

    def __str__(self):
        return f'Nombre: {self.nombre}'

    def generar_dic(self):
        return {'nombre': self.nombre, 'clave': self.clave}

    def cambiar_clave(self, cosa):
        self.clave = cosa


class Producto:
    def __init__(self, nombre, cantidad, precio):
        self.precio = precio
        self.cantidad = int(cantidad)
        self.nombre = nombre

    def generar_dic(self):
        return {'nombre': self.nombre, 'cantidad': self.cantidad, 'precio': self.precio}

    def cambiar_informacion(self, dato, cant):
        if dato == 'cantidad':
            self.cantidad = int(cant)
        elif dato == 'precio':
            self.precio = cant

    def __str__(self):
        return f'Producto: {self.nombre}\nCantidad: {self.cantidad} unidades\nPrecio: {self.precio} pesos'

    def informacion(self):
        return print(self)


# Funciones


def agregar_a_gondola(prod, cant, prec):
    item = Producto(prod, cant, prec)
    gondola.append(item)
    print(gondola)


def agregar_a_carro(pro, cant):
    cant = int(cant)
    for a in gondola:
        if a.nombre == pro and a.cantidad > cant:
            val = a.precio
            item = Producto(pro, cant, val)
            carro.append(item)
            a.cantidad -= cant


def agregar_empleado(nom, psw):
    laburante = Empleado(nom, psw)
    empleados.append(laburante)


def eliminar_de_gondola(producto):
    for i in gondola:
        if i.nombre == producto:
            gondola.remove(i)


def eliminar_de_carro(producto):
    for i in carro:
        if i.nombre == producto:
            carro.remove(i)


def pagar():
    total = 0
    for i in carro:
        total += i.cantidad * i.precio
    print(f'Usted debe pagar {total} pesos')


def hacer_visible(cosa):
    listita = []
    if cosa == 'gondola':
        for prod in gondola:
            listita.append(prod.generar_dic())
        print(listita)
    elif cosa == 'carro':
        for prod in carro:
            listita.append(prod.generar_dic())
        print(listita)
    else:
        for emp in empleados:
            listita.append(emp.generar_dic())
        print(listita)


# Cuerpo

gondola = []

empleados = []
while True:
    agregar_empleado('jefe', '1234')
    carro = []
    print('\n\tBienvenido al Kiosco digital')
    print('\nSi es consumidor ingrese 1')
    print('Si es repositor ingrese 2')

    try:
        ingreso = int(input('>> '))

        if ingreso == 1:
            while True:
                print('\nQue accion desea realizar')
                print('1) Revisar gondola')
                print('2) Agregar al carro')
                print('3) Revisar carro')
                print('4) Eliminar del carro')
                print('5) Pagar')
                print('6) Salir')

                try:
                    num = int(input('>> '))

                    if num == 1:
                        hacer_visible('gondola')
                    elif num == 2:
                        agregar_a_carro(input('Producto '), input('Cantidad '))
                    elif num == 3:
                        hacer_visible('carro')
                    elif num == 4:
                        eliminar_de_carro(input('Producto '))
                    elif num == 5:
                        pagar()
                        break
                    else:
                        break
                except:
                    print("\nDebe ingresar numeros, no letras")

        elif ingreso == 2:
            print('\nNombre')
            usr = input(">> ")
            print("\nIngresar su clave")
            pasw = input(">> ")

            for empleado in empleados:
                if empleado.nombre == usr and empleado.clave == pasw:
                    while True:
                        print('\nQue accion desea realizar')
                        print('1) Revisar gondola')
                        print('2) Agregar a gondola')
                        print('3) Eliminar de gondola')
                        print('4) Cambiar dato de producto')
                        print('5) Salir')
                        if usr == 'jefe':
                            print('6) Contratar empleado')
                            print('7) Editar clave de empleado')
                            print('8) Empleados')

                        try:
                            numero = int(input('>> '))

                            if numero == 1:
                                hacer_visible('gondola')
                            elif numero == 2:
                                agregar_a_gondola(input('Producto '), int(input('Cantidad ')), int(input('Precio ')))
                            elif numero == 3:
                                eliminar_de_gondola(input('>> '))
                            elif numero == 4:
                                prod = input('Ingrese producto ')
                                for i in gondola:
                                    if i.nombre == prod:
                                        i.cambiar_informacion(input('Que desea cambiar '), input('>> '))
                            elif numero == 5:
                                break
                            elif numero == 6 and usr == 'jefe':
                                agregar_empleado(input('Nombre '), input('Clave '))
                            elif numero == 7 and usr == 'jefe':
                                em = input('Empleado ')
                                for i in empleados:
                                    if i.nombre == em:
                                        i.cambiar_clave(input('>> '))
                            elif numero == 8 and usr == 'jefe':
                                hacer_visible('empleados')
                        except:
                            print("\nDebe ingresar numeros, no letras")
                else:
                    print('Usuario o clave no validos')
        else:
            print('\nIngrese un numero valido')
    except:
        print("\nDebe ingresar numeros, no letras")