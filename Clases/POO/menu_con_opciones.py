from crear_tabla import get_db
from Usuario import Persona


def bienvenida():
    print('\t\t @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
    print('\t\t @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
    print('\t\t @@    La Rotiseria      @@')
    print('\t\t @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
    print('\t\t @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')

def menu():
    print('\n\t ----[MENU]---------')
    print('\t 1) Agregar al menu')
    print('\t 2) Actualizar menu')
    print('\t 3) Borrar menu')
    print('\t 4) Consultar un menu')
    print('\t 5) Consultar todos los menues')
    print('\t 6) Salir')


def insert_menu(menu_code, Nombre, descripcion, precio):
    db = get_db()
    cursor = db.cursor()
    statement = "INSERT INTO menues (menu_code, Nombre, descripcion, precio) \
    VALUES ( ?, ?, ?, ?)"
    cursor.execute(statement, [menu_code, Nombre, descripcion, precio])
    db.commit()
    return True

def update_menu(menu_code, Nombre, descripcion, precio):
    db = get_db()
    cursor = db.cursor()
    statement = "UPDATE menues SET Nombre = ?, descripcion = ?\
    WHERE menu_code = ?"
    cursor.execute(statement, [Nombre, descripcion, precio])
    db.commit()
    return True


def delete_menu(menu_code):
    db = get_db()
    cursor = db.cursor()
    statement = "DELETE FROM menues WHERE menu_code = ?"
    cursor.execute(statement, [menu_code])
    db.commit()
    return True


def get_by_id(menu_code):
    db = get_db()
    cursor = db.cursor()
    statement = "SELECT menu_code, Nombre, descripcion, precio FROM menues \
    WHERE menu_code = ?"
    cursor.execute(statement, [menu_code])
    single_menu = cursor.fetchone()
    menu_code = single_menu[0]
    Nombre = single_menu[1]
    descripcion = single_menu[2]
    precio = single_menu[3]
    menu = Menu (menu_code, Nombre, descripcion, precio)
    return menu.serialize_details()


def get_menues():
    db = get_db()
    cursor = db.cursor()
    query = "SELECT menu_code, Nombre, descripcion, precio FROM menues"
    cursor.execute(query)
    menu_list = cursor.fetchall()
    list_of_menues=[]
    for menu in menu_list:
        menu_code = menu[0]
        Nombre = menu[1]
        descripcion = menu[2]
        precio = menu[3]
        menu_to_add = Menu(menu_code, Nombre, descripcion, precio)
        list_of_menues.append(menu_to_add)
    return list_of_menues

def salir():
    print('Gracias por utilizar nuestro servicios')

bienvenida()

while True:
    try:
        menu()
        opcion = int(input("Ingrese una Opcion: "))
        if opcion==1:
            insert_menu()
        elif opcion==2:
            update_menu()
        elif opcion==3:
            delete_menu()
        elif opcion==4:
            get_by_id()
        elif opcion==5:
            get_menues()
        elif opcion==6:
            salir()
            break
    except:
        print('Excepcion! opciones validas son (1 hasta 5 y 6 para Salir)')