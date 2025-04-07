class Producto:
    def __init__(self, nombre, descripcion, cantidad, precio_unitario, categoria):
        self.nombre = nombre
        self.descripcion = descripcion
        self.cantidad = cantidad
        self.precio_unitario = precio_unitario
        self.categoria = categoria

class Usuario:
    def __init__(self, username, password):
        self.username = username
        self.password = password  
