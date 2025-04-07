import sqlite3
from app.utils import log_info, log_error

def agregar_producto(producto):
    try:
        conn = sqlite3.connect('inventario.db')
        c = conn.cursor()
        c.execute('''INSERT INTO productos (nombre, descripcion, cantidad, precio, categoria) VALUES (?, ?, ?, ?, ?)''', 
            (producto.nombre, producto.descripcion, producto.cantidad, producto.precio_unitario, producto.categoria))
        conn.commit()
        log_info(f"Producto agregado: {producto.nombre}")
    except Exception as e:
        log_error(f"Error al agregar producto: {e}")
    finally:
        conn.close()

def listar_productos():
    try:
        conn = sqlite3.connect('inventario.db')
        c = conn.cursor()
        c.execute('SELECT * FROM productos')
        productos = c.fetchall()
        return productos
    except Exception as e:
        log_error(f"Error al listar productos: {e}")
        return []
    finally:
        conn.close()

def actualizar_producto(id_producto, nuevos_datos):
    conn = sqlite3.connect('inventario.db')
    c = conn.cursor()
    c.execute('''
        UPDATE productos
        SET nombre = ?, descripcion = ?, cantidad = ?, precio = ?, categoria = ?
        WHERE id = ?
    ''', (nuevos_datos['nombre'], nuevos_datos['descripcion'], nuevos_datos['cantidad'],
            nuevos_datos['precio'], nuevos_datos['categoria'], id_producto))
    conn.commit()
    conn.close()

def eliminar_producto(id_producto):
    conn = sqlite3.connect('inventario.db')
    c = conn.cursor()
    c.execute('DELETE FROM productos WHERE id = ?', (id_producto,))
    conn.commit()
    conn.close()
