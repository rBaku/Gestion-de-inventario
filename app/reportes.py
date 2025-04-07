import sqlite3
from app.utils import log_info, log_error

def valor_total_inventario():
    try:
        conn = sqlite3.connect('inventario.db')
        c = conn.cursor()
        c.execute('SELECT SUM(cantidad * precio) FROM productos')
        total = c.fetchone()[0]
        return total or 0
    except Exception as e:
        log_error(f"Error al calcular valor inventario: {e}")
        return 0
    finally:
        conn.close()

def productos_agotados():
    try:
        conn = sqlite3.connect('inventario.db')
        c = conn.cursor()
        c.execute('SELECT * FROM productos WHERE cantidad = 0')
        return c.fetchall()
    except Exception as e:
        log_error(f"Error al obtener productos agotados: {e}")
        return []
    finally:
        conn.close()