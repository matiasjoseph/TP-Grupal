class Persona:
    nombre = ''
    edad = 0

    def __init__(self, nombre, apllido, mail, edad):
        self.nombre = nombre
        self.edad = edad
        self.apellido = apellido
        self.mail = mail
        self.menu_elegido = None
        self.hora_elegida = None
    def __str__(self):
        return 'Persona: ' + self.nombre + ' edad: ' + str(self.edad)
    
    def ingresar(self):
        print(f"{self.mail} ha ingresado correctamente!")
        print(f"\n ¡Bienvenido/a {self.nombre}, " ", {self.apellido}")
              
    def comprar(self):
        personas = []
        menu_elegido = int(input("Seleccione el numero del menú que desea: "))
        hora_elegida = int(input("Seleccione la hora en la que desea recibir el menú: "))
        persona.menu_elegido = menu_elegido
        persona.hora_elegida = hora_elegida

