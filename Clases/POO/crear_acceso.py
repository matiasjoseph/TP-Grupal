#en la base de datos vamos a escribir todos los usuarios de los alumons/profesores de la Ucema. Cada vez que un alumno ingrese, sera actualizada la base de datos. El objetivo es que esta aplicacion sea solo utilizada por los alumnos/profesores de la Ucema. 
base_de_datos = {}

f = open("mi_bd.csv","a")
usuario_ingresado = input("Usuario: ")
contraseña_ingresada = input("Contraseña: ")

f.write(f"{usuario_ingresado}, {contraseña_ingresada}\n")

f.close()

base_de_datos = {"usuario_ingresado":"contraseña_ingresada"}

def login(usuario,contraseña):
    if usuario_ingresado in base_de_datos and base_de_datos.get(usuario) == contraseña:
        return("se ha ingresado correctamente")
    else:
        return("el usuario o la contraseña son incorrectas")
  
