import sqlite3
DATABASE_NAME = "menues.db"


def get_db():
    conn = sqlite3.connect(DATABASE_NAME)
    return conn


def create_tables():
    tables = [
        """CREATE TABLE IF NOT EXISTS menues(
                menu_code INTEGER PRIMARY KEY,
                Nombre TEXT NOT NULL,
                descripcion TEXT NOT NULL,
                precio INTEGER NOT NULL,
            )
            """
    ]
    db = get_db()
    cursor = db.cursor()
    for table in tables:
        cursor.execute(table)