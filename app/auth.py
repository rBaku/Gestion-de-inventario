import sqlite3

def crear_usuario(username, password):
    conn = sqlite3.connect('inventario.db')
    c = conn.cursor()
    try:
        c.execute('INSERT INTO usuarios (username, password) VALUES (?, ?)', (username, password))
        conn.commit()
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()
    return True

def login(username, password):
    conn = sqlite3.connect('inventario.db')
    c = conn.cursor()
    c.execute('SELECT * FROM usuarios WHERE username = ? AND password = ?', (username, password))
    usuario = c.fetchone()
    conn.close()
    return usuario is not None
