import sqlite3

def agregar_producto(producto):
    conn = sqlite3.connect('inventario.db')
    c = conn.cursor()
    c.execute('''
        INSERT INTO productos (nombre, descripcion, cantidad, precio, categoria)
        VALUES (?, ?, ?, ?, ?)
    ''', (producto.nombre, producto.descripcion, producto.cantidad, producto.precio_unitario, producto.categoria))
    conn.commit()
    conn.close()

def listar_productos():
    conn = sqlite3.connect('inventario.db')
    c = conn.cursor()
    c.execute('SELECT * FROM productos')
    productos = c.fetchall()
    conn.close()
    return productos

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
