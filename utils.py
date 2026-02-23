"""
Lógica de apoyo a main
"""


def mostrar_menu():
    """
    Función para mostrar el menú de opciones
    """
    print("+---------------------------+")
    print("| 📦Inventario app          |")
    print("+---------------------------|")
    print("| 1 - Agregar producto.     |")
    print("| 2 - Venta producto.       |")
    print("| 3 - Resumen inventario.   |")
    print("| 4 - Borrar inventario.    |")
    print("| 5 - Salir.                |")
    print("+---------------------------+\n")


def validar_opcion(msg_input: str, msg_error: str) -> int:
    """
    Funcion para verificar opcion de entrada

    Args:
        msg_input (str): Mensaje de input
        msg_error (str): Mensaje de error

    Return:
        (int): opcion validada
    """
    while True:
        try:
            opcion = input(msg_input)
            opcion = int(opcion)
            break
        except ValueError:
            print(msg_error)
    return opcion


def leer_cadenas(msg_imput: str, msg_error: str) -> str:
    """
    Función para verifcar el texto en formato correcto.
    Sin espacios y que no sea una cadena vacía.

    Args:
        msg_imput (str): Mensaje de input.
        msg_error (str): mensaje de error.

    Returns:
        str: texto con formato correcto.
    """
    while True:
        texto = input(msg_imput).lower()
        try:
            if not texto.strip():
                raise ValueError(msg_error)
        except ValueError as e:
            print(f"❌ ERROR: {e}")
        else:
            break
    return texto


def validacion_dato(msg_input: str, msg_error_neg: str, msg_error: str, tipo_dato: type):
    """
    Funció para validar datos

    Args:
        msg_input (str): Mensaje de input
        msg_error_neg (str): Mensaje de error, precio negativo.
        msg_error (str): Mensaje de error generico
        tipo_dato (_type_): Tipo de dato esperado.

    Returns:
        float: Dato con formato correcto de moneda
    """
    while True:
        dato = input(msg_input)
        try:
            dato = tipo_dato(dato)
            if dato < 0:
                print(msg_error_neg)
                continue
            break
        except ValueError:
            print(f"❌ ERROR: {msg_error}")
    return dato


def mostrar_resumen(resumen: dict):
    """
    Función para mostrar el resumen formateado

    Args:
        resumen (dict): Diccionario donde se almacena el inventario
    """
    print("+----------------------------------------------+")
    print("| ✍ Resumen de inventario                     |")
    print("+----------------------------------------------+")
    print(
        f" - Total de articulos en almácen: {resumen['unidades_totales']}")
    print(f" - Valor total del almácen: {resumen['valor_total']}")


def mostrar_venta(exito: bool, nombre: str, cantidad: int, inventario: dict):
    """
    Función para mostrar si la venta se ha efectuado correctamente

    Args:
        exito (bool): Resultado de la venta
        nombre (str): Nombre del producto
        cantidad (int): Cantidad a vender
        inventario (dict): Diccionario donde se almacenan los productos de la inventarios
    """
    precio_unidad = inventario[nombre]['precio']
    total_venta = precio_unidad * cantidad
    if exito:
        print("✅Venta efectuada: ")
        print(f" - Nombre: {nombre}")
        print(f" - Cantidad: {cantidad}")
        print(
            f" - Total venta: {total_venta:.2f} €\n")
    else:
        print("📛No es posible efectura la venta: ")
        print("Stock insuficiente o no se encuentra producto")
