from crear_tabla import get_db
from Usuario import Persona


def insert_menu(menu_code, nombre, descripcion, precio):
    db = get_db()
    cursor = db.cursor()
    statement = "INSERT INTO menues (menu_code, nombre, descripcion, precio) \
    VALUES ( ?, ?, ?, ?)"
    cursor.execute(statement, [menu_code, nombre, descripcion, precio])
    db.commit()
    return True

def update_menu(menu_code, nombre, descripcion, precio):
    db = get_db()
    cursor = db.cursor()
    statement = "UPDATE menues SET nombre = ?, descripcion = ?\
    WHERE menu_code = ?"
    cursor.execute(statement, [nombre, descripcion, precio])
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
    statement = "SELECT menu_code, nombre, descripcion, precio FROM menues \
    WHERE menu_code = ?"
    cursor.execute(statement, [menu_code])
    single_menu = cursor.fetchone()
    menu_code = single_menu[0]
    nombre = single_menu[1]
    descripcion = single_menu[2]
    precio = single_menu[3]
    menu = Menu (menu_code, nombre, descripcion, precio)
    return menu.serialize_details()


def get_menues():
    db = get_db()
    cursor = db.cursor()
    query = "SELECT menu_code, nombre, descripcion, precio FROM menues"
    cursor.execute(query)
    menu_list = cursor.fetchall()
    list_of_menues=[]
    for menu in menu_list:
        menu_code = menu[0]
        nombre = menu[1]
        descripcion = menu[2]
        precio = menu[3]
        menu_to_add = Menu(menu_code, nombre, descripcion, precio)
        list_of_menues.append(menu_to_add)
    return list_of_menues




