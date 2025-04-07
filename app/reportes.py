def resumen(inventario):
    total_productos = len(inventario)
    valor_total = sum(p.cantidad * p.precio_unitario for p in inventario)
    agotados = [p for p in inventario if p.cantidad == 0]
    return total_productos, valor_total, agotados
