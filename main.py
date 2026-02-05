from inventario_logic import agregar_producto, vender_producto, obtener_resumen
from utils import mostrar_menu, leer_cadenas, validar_opcion, validacion_dato, mostrar_venta, mostrar_resumen

# ---- CONSTANTES MSG  -----
INPUT_OPCION = "➡ Introduzca una opción: "
INPUT_NOMBRE = "Nombre del producto: "
INPUT_CANT = "Cantidad del producto: "
INPUT_PREC = "Precio del producto (2 decimales): "

# ---- CONSTANTES ERR ----
ERROR_OPCION = "🛑 El valor introducido debe ser un número entero..."
ERROR_NOMBRE = "🛑 No has introducido un nombre..."
ERROR_PREC_NEG = "🛑 El precio no puede ser negativo..."
ERROR_CANT_NEG = "🛑 La cantidad no puede ser negativa..."
ERROR_DATO_INV = "ERROR: ❌ no es un valor válido, intentelo de nuevo."

# Función principal de programa


def ejecutar_inventario():
    """
    Función princpial para ejecutar el programa y su funcionalidad
    """
    # Diccionario vacío para almacenar el inventario del almácen
    inventario = {}
    while True:
        # Mostramos menú
        mostrar_menu()
        # Solicitamos opción y validamos
        opcion = validar_opcion(INPUT_OPCION, ERROR_OPCION)
        match opcion:
            case 1:
                # Leer nombre validado
                nombre = leer_cadenas(INPUT_NOMBRE, ERROR_NOMBRE)
                # validar cantidad
                cantidad = validacion_dato(
                    INPUT_CANT, ERROR_CANT_NEG, ERROR_DATO_INV, int)
                # Validar precio
                precio = validacion_dato(
                    INPUT_PREC, ERROR_PREC_NEG, ERROR_DATO_INV, float)
                # Agregar producto
                agregar_producto(nombre, precio, cantidad, inventario)
                # Mensaje de confirmación.
                print("✅ Producto añadido o modificado\n")
            case 2:
                # Solicitamos datos del producto a vender
                # Validación de nombre de producto
                nombre = leer_cadenas(INPUT_NOMBRE, ERROR_NOMBRE)
                # Validación de Cantidad de venta
                cantidad = validacion_dato(
                    INPUT_CANT, ERROR_CANT_NEG, ERROR_DATO_INV, int)
                # Comprobamos si se puede realizar la venta:
                exito = vender_producto(nombre, cantidad, inventario)
                # Mostra informacion de venta
                mostrar_venta(exito, nombre, cantidad, inventario)
            case 3:
                # Llamamamos a lógica de metricas de inventario
                resumen = obtener_resumen(inventario)
                # Mostrar resumen
                mostrar_resumen(resumen)


if __name__ == "__main__":
    ejecutar_inventario()
