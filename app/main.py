from app import db, auth, crud
from app.models import Producto

def menu():
    db.crear_tablas()
    print("Bienvenido al sistema de inventario")

    username = input("Usuario: ")
    password = input("Contraseña: ")

    if not auth.login(username, password):
        print("Usuario no registrado. Registrando nuevo usuario...")
        if auth.crear_usuario(username, password):
            print("Usuario creado exitosamente.")
        else:
            print("Error al crear usuario.")
            return

    while True:
        print("\n1. Agregar producto")
        print("2. Ver productos")
        print("3. Actualizar producto")
        print("4. Eliminar producto")
        print("5. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            nombre = input("Nombre: ")
            descripcion = input("Descripción: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            categoria = input("Categoría: ")
            producto = Producto(nombre, descripcion, cantidad, precio, categoria)
            crud.agregar_producto(producto)
            print("Producto agregado.")
        elif opcion == '2':
            productos = crud.listar_productos()
            for p in productos:
                print(p)
        elif opcion == '3':
            id_p = int(input("ID del producto a actualizar: "))
            nuevos_datos = {
                "nombre": input("Nuevo nombre: "),
                "descripcion": input("Nueva descripción: "),
                "cantidad": int(input("Nueva cantidad: ")),
                "precio": float(input("Nuevo precio: ")),
                "categoria": input("Nueva categoría: ")
            }
            crud.actualizar_producto(id_p, nuevos_datos)
            print("Producto actualizado.")
        elif opcion == '4':
            id_p = int(input("ID del producto a eliminar: "))
            crud.eliminar_producto(id_p)
            print("Producto eliminado.")
        elif opcion == '5':
            print("Saliendo...")
            break
        else:
            print("Opción inválida")

if __name__ == "__main__":
    menu()
