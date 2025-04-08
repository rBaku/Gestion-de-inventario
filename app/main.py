from app import db, auth, crud, reportes
from app.models import Producto

def menu():
    db.crear_tablas()
    print("=== Bienvenido al sistema de inventario ===")

    username = input("Usuario: ")
    password = input("Contraseña: ")

    if not auth.login(username, password):
        print("Usuario no registrado. Registrando nuevo usuario...")
        if not auth.crear_usuario(username, password):
            print("No se pudo crear el usuario.")
            return

    while True:
        print("\n1. Agregar producto\n2. Listar productos\n3. Valor total inventario\n4. Productos agotados\n5. Salir")
        opcion = input("Opción: ")

        if opcion == '1':
            try:
                nombre = input("Nombre: ")
                descripcion = input("Descripción: ")
                cantidad = int(input("Cantidad: "))
                if cantidad < 0:
                    raise ValueError("La cantidad no puede ser negativa.")
                precio = float(input("Precio: "))
                categoria = input("Categoría: ")
                producto = Producto(nombre, descripcion, cantidad, precio, categoria)
                crud.agregar_producto(producto)
            except Exception as e:
                print(f"Error: {e}")
        elif opcion == '2':
            productos = crud.listar_productos()
            for p in productos:
                print(p)
        elif opcion == '3':
            total = reportes.valor_total_inventario()
            print(f"Valor total del inventario: ${total:.2f}")
        elif opcion == '4':
            agotados = reportes.productos_agotados()
            print("Productos agotados:")
            for a in agotados:
                print(a)
        elif opcion == '5':
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida")

if __name__ == "__main__":
    menu()
