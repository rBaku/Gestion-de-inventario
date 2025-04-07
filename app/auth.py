import sqlite3
from app.utils import log_info, log_error

def crear_usuario(username, password):
    try:
        conn = sqlite3.connect('inventario.db')
        c = conn.cursor()
        c.execute('INSERT INTO usuarios (username, password) VALUES (?, ?)', (username, password))
        conn.commit()
        log_info(f"Usuario creado: {username}")
        return True
    except sqlite3.IntegrityError:
        log_error("Nombre de usuario ya existe.")
        return False
    except Exception as e:
        log_error(f"Error creando usuario: {e}")
        return False
    finally:
        conn.close()

def login(username, password):
    try:
        conn = sqlite3.connect('inventario.db')
        c = conn.cursor()
        c.execute('SELECT * FROM usuarios WHERE username = ? AND password = ?', (username, password))
        if c.fetchone():
            log_info(f"Login exitoso: {username}")
            return True
        else:
            log_info(f"Login fallido: {username}")
            return False
    except Exception as e:
        log_error(f"Error durante login: {e}")
        return False
    finally:
        conn.close()