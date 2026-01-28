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
        print("| 3- Resumen inventario.    |")
        print("| 4 - Salir.                |")
        print("+---------------------------+\n")
        # Solicitamos opción:
        opcion = int(input("➡ Introduzca una opción: \n"))
        # Evaluamos opción
        match opcion:
            case 1:
                nombre = input("Nombre del producto: ").lower()
                precio = float(input("Precio del producto (2 decimales): "))
                cantidad = int(input("Cantidad del producto: "))
                # Llamamos a nuestra lógica de entrada
                agregar_producto(nombre, precio, cantidad, inventario)
                print("✅ Producto añadido o modificado\n")
            case 2:
                # Solicitamos datos del producto a vender
                nombre = input("Nombre del producto a vender: ").lower()
                cantidad = int(input("Cantida a vender: "))
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
