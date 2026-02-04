from inventario_logic import agregar_producto, vender_producto, obtener_resumen


# Función principal de programa
def ejecutar_inventario():
    """
    Función princpial para ejecutar el programa y su funcionalidad
    """
    # Diccionario vacío para almacenar el inventario del almácen
    inventario = {}
    while True:
        # Mostramos menú
        print("+---------------------------+")
        print("| 📦Inventario app          |")
        print("+---------------------------|")
        print("| 1 - Agregar producto.     |")
        print("| 2 - Venta producto.       |")
        print("| 3 - Resumen inventario.   |")
        print("| 4 - Salir.                |")
        print("+---------------------------+\n")
        # Solicitamos opción:
        while True:
            try:
                opcion = int(input("➡ Introduzca una opción: \n"))
                break
            except ValueError:
                print("🛑 El valor introducido debe ser un número entero.")
        # Evaluamos opción
        match opcion:
            case 1:
                while True:
                    nombre = input("Nombre del producto: ").lower()
                    try:
                        if not nombre.strip():
                            raise ValueError(
                                "🛑 No has introducido un nombre...")
                        else:
                            break
                    except ValueError as e:
                        print(f"ERROR: {e}")
                # Validación de precio, con bucle
                while True:
                    precio = input("Precio del producto (2 decimales): ")
                    try:
                        precio = float(precio)
                        if precio < 0:
                            print("🛑 El precio no puede ser negativo")
                            continue
                        break
                    except ValueError:
                        print("ERROR: ❌ no es un valor válido, intentelo de nuevo")
                # Validación de cantidad con bucle
                while True:
                    cantidad = input("Cantidad del producto: ")
                    try:
                        cantidad = int(cantidad)
                        if cantidad < 0:
                            print("🛑 La cantidad no puede ser negativa.")
                            continue
                        break
                    except ValueError:
                        print("ERROR: ❌ no es un valor válido, intentelo de nuevo")
                # Llamamos a nuestra lógica de entrada
                agregar_producto(nombre, precio, cantidad, inventario)
                print("✅ Producto añadido o modificado\n")
            case 2:
                # Solicitamos datos del producto a vender
                # Validación de nombre de producto
                while True:
                    nombre = input("Nombre del producto: ").lower()
                    try:
                        if not nombre.strip():
                            raise ValueError(
                                "🛑 No has introducido un nombre...")
                        else:
                            break
                    except ValueError as e:
                        print(f"ERROR: {e}")
                # Validación de Cantidad de venta
                while True:
                    cantidad = input("Cantidad del producto: ")
                    try:
                        cantidad = int(cantidad)
                        if cantidad < 0:
                            print("🛑 La cantidad no puede ser negativa.")
                            continue
                        break
                    except ValueError:
                        print("ERROR: ❌ no es un valor válido, intentelo de nuevo")
                # Comprobamos si se puede realizar la venta:
                exito = vender_producto(nombre, cantidad, inventario)
                if exito:
                    print("✅Venta efectuada: ")
                    print(f" - Nombre: {nombre}")
                    print(f" - Cantidad: {cantidad}")
                    print(
                        f" - Total venta: {inventario[nombre]['precio']*cantidad} €\n")
                else:
                    print("📛No es posible efectura la venta: ")
                    print("Stock insuficiente o no se encuentra producto")

            case 3:
                # Llamamamos a lógica de metricas de inventario
                resumen = obtener_resumen(inventario)
                print("+----------------------------------------------+")
                print("| ✍ Resumen de inventario                     |")
                print("+----------------------------------------------+")
                print(
                    f" - Total de articulos en almácen: {resumen['unidades_totales']}")
                print(f" - Valor total del almácen: {resumen['valor_total']}")
            case 4:
                print("Saliendo del programa....🖐")
                break
            case _:
                print("❌ Opción no válida")


if __name__ == "__main__":
    ejecutar_inventario()
