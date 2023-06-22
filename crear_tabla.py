import sqlite3
DATABASE_NAME = "menues.db"


def get_db():
    conn = sqlite3.connect(DATABASE_NAME)
    return conn


def create_tables():
    tables = [
        """CREATE TABLE IF NOT EXISTS menues(
                menu_code INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                descripcion TEXT NOT NULL,
                precio INTEGER NOT NULL
            )
            """
    ]
    db = get_db()
    cursor = db.cursor()
    for table in tables:
        cursor.execute(table)

def seed_comidas():
    queries = ["INSERT OR IGNORE INTO menues (menu_code, nombre, descripcion, precio) VALUES (1, 'Pizza de Muzzarella', 'Salsa de tomate y queso Muzarella', 3200)",
               "INSERT OR IGNORE INTO menues (menu_code, nombre, descripcion, precio) VALUES (2, 'Pizza de Jamon y Morrones', 'Salsa de tomate, jamón y morrones', 3500)",
               "INSERT OR IGNORE INTO menues (menu_code,  nombre, descripcion, precio) VALUES (3, 'Pizza de Fugazzeta', 'Cebolla, Queso Muzzarella y Aceitunas', 3500)",
               ]
    db = get_db()
    cursor = db.cursor()
    for query in queries:
        cursor.execute(query)
    db.commit()
