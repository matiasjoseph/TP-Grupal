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

class Comida:
    def __init__(self, nombre, descripcion, precio):
        self.precio = precio
        self.nombre = nombre
        self.descripcion = descripcion

    def generar_dic(self):
        return {'nombre': self.nombre, 'descripcion': self.descripcion, 'precio': self.precio}

    def cambiar_informacion(self, dato, cant):
        if dato == 'precio':
            self.precio = cant

    def __str__(self):
        return f'nombre: {self.nombre}\ndescripcion: {self.descripcion} \nprecio: {self.precio} pesos'

    def informacion(self):
        return print(self)


# Funciones


def agregar_a_carta(pro, cant, precio):
    cant = int(cant)
    for a in cocina:
        if a.nombre == pro and a.cantidad > cant:
            val = a.precio
            item = Comida(pro, cant, val)
            stock.append(item)
            a.cantidad -= cant


def inicio_empleado(nom, psw):
    laburante = Empleado(nom, psw)
    empleados.append(laburante)


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
    else:
        for emp in empleados:
            listita.append(emp.generar_dic())
        print(listita)

def salir():
    print('Gracias por utilizar nuestro servicios')

# Cuerpo

cocina = []

empleados = []

Flag = True


while Flag:
    inicio_empleado('gerente', '1234')
    stock = []
    print('\nBienvenido a la Rotiseria')

    try:

        print('\nNombre')
        usr = input(">> ")
        print("\nIngresar su clave")
        pasw = input(">> ")

        for empleado in empleados:
            if empleado.nombre == usr and empleado.clave == pasw:
                while Flag:
                    print('\nQue accion desea realizar')
                    print('1) Revisar stock')
                    print('2) Agregar a la carta')
                    print('3) Eliminar de la carta')
                    print('4) Cambiar dato de comida')
                    print('5) Pagar')
                    print('6) Salir')



                    try:
                        num = int(input('>> '))

                        if num == 1:
                            hacer_visible('cocina')
                        elif num == 2:
                            agregar_a_carta(input('Nombre del Plato: '), input('Cantidad: '), input('Precio: '))
                        elif num == 3:
                            eliminar_de_carta(input('Que plato desea eliminar?: '))
                        elif num == 4:
                            prod = input('Ingrese un producto para cambiarlo: ')
                            for i in cocina:
                                if i.nombre == prod:
                                    i.cambiar_informacion(input('Que desea cambiar? '), input('>> '))
                        elif num == 5:
                            pagar()
                        elif num == 6:
                            salir()
                            Flag = False
                        else:
                            break
                    except Exception as e:
                        print('Debe ingresar numeros, no letras', e)
            else:
                print('Usuario o clave no validos. Ingrese de nuevo')

    except Exception as e:
        print('Debe ingresar numeros, no letras', e)