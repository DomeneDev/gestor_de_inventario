"""
Funciones puras que gestionarán los datos del almacén .
El inventaario se esctructurará como un diccionario de diccionarios:
{"nombre":
    {
    "precio":float,
    "cantidad": int
    }
}
"""


def agregar_producto(nombre: str, precio: float, cantidad: int, inventario: dict):
    """
    Función de registro y/o actualización de productos.

    Args:
        nombre (str): Nombre del producto
        precio (float): Precio del producto
        cantidad (int): Cantidad del producto
        inventario (dict): Diccionario de Diccionarios donde se alamcena el inventario.
    """
    # Si no existe lo generaamos y añadimos al diccionario inventario
    if nombre not in inventario.keys():
        datos_producto = {"precio": precio, "cantidad": cantidad}
        inventario[nombre] = datos_producto
    # Si si existe, modificamos los datos de cantidad y precio
    else:
        inventario[nombre]["cantidad"] += cantidad
        inventario[nombre]["precio"] = precio


def vender_producto(producto: str, cantidad_venta: int, inventario: dict) -> bool:
    """
    Función de salida de productos.

    Args:
        producto (str): Producto a vender.
        cantidad_venta (int): Cantidad a vender.
        invetario (dict): Diccionario de Diccionarios donde se alamcena el inventario.

    Returns:
        bool: True si la salida se puede realizar, False en caso contrario.
    """
    # Comprobamos si el producto existe
    if producto in inventario.keys():
        # Si hay suficiente cantidad para la venta, actualizamos stock y devolvemos True
        if cantidad_venta <= inventario[producto]["cantidad"]:
            inventario[producto]["cantidad"] -= cantidad_venta
            return True
        # Si no devolvemos False
        else:
            return False


def obtener_resumen(inventario: dict) -> dict:
    """
    Función para calcular el valor del stock del inventario.

    Args:
        iventario (dict): Diccionario de Diccionarios donde se alamcena el inventario.

    Returns:
        dict: Diccionarío de métricas de producto/ valor.
    """
    # Establecemos variables para almacenar los valores de valor total y total unidades
    valor_total_inventario = 0
    unidades_fisicas_almacen = 0
    # Recorrecmos el diccionario extrayendo los datos
    for datos in inventario.values():
        cantidad = datos["cantidad"]
        valor = datos["precio"]
        valor_stock = valor * cantidad
        # Almacenamos los datos en las variables
        unidades_fisicas_almacen += cantidad
        valor_total_inventario += valor_stock
    # Generamos el diccionario para almacenar las métricas
    metricas = {
        "valor_total": round(valor_total_inventario, 2),
        "unidades_totales": unidades_fisicas_almacen
    }
    # Devolvemos diccionario con métricas
    return metricas
