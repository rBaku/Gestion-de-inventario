import sqlite3
from app.utils import log_info, log_error
def crear_tablas():
    try:
        conn = sqlite3.connect('inventario.db')
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS productos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT,
                descripcion TEXT,
                cantidad INTEGER,
                precio REAL,
                categoria TEXT
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE,
                password TEXT
            )
        ''')
        conn.commit()
        log_info("Tablas creadas o verificadas correctamente.")
    except Exception as e:
        log_error(f"Error al crear tablas: {e}")
    finally:
        conn.close()