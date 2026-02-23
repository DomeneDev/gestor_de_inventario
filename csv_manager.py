"""
Fichero para almacenar funciones de comunicación y trabajos sobre el disco duro
"""

# biblioteca para trabajos con CSV
import csv


def guardar_csv(inventario: dict, ruta: str, msg_error: str):
    """
    Función para guardar el inventario

    Args:
        inventario (dict): Diccionario de diccionarios donde se almacenan los
        productos
        ruta (str): Ruta donde se almacena el fichero .csv
        msg_error (str): Mensaje de error si el archivo no se encuentra
    """
    try:
        # Definimos los campos del fichero csv
        campos = ['nombre', 'precio', 'cantidad']
        with open(ruta, 'w', newline="", encoding='utf-8') as f:
            # generamos un escritor
            escritor = csv.DictWriter(f, fieldnames=campos)
            # Escribimos la cabecera
            escritor.writeheader()
            # Recorremos el inventario, diccionario de diccionarios
            for nombre, datos in inventario.items():
                # Establecemos los datos de la fila
                fila = {
                    "nombre": nombre,
                    "precio": datos['precio'],
                    "cantiad": datos['cantidad']
                }
                # Escribimos la fila
                escritor.writerow(fila)
    except FileNotFoundError:
        print(msg_error)


def cargar_csv(ruta: str) -> dict:
    """
    Función para cargar el inventario en el programa, leerá el archivo csv y
    generar un diccionario de diccionarios

    Args:
        ruta (str): Ruta donde se debe encontrar el archivo .csv

    Returns:
        dict: Diccionario de inventario
    """
    # Variable invenatariio para almacenar el diccionario de diccionarios.
    inventario = {}
    # Control del error por si el archivo no existe
    try:
        with open(ruta, 'r', newline="", encoding='utf-8') as f:
            # Generamos lector
            lector = csv.DictReader(f)
            # Recorremos el fichero con el lector
            for fila in lector:
                nombre = fila['nombre']
                precio = float(fila['precio'])
                cantidad = int(fila['cantidad'])
                # Generamos el fichero inventario
                inventario[nombre] = {
                    'precio': precio,
                    'cantiad': cantidad
                }
            return inventario
    except FileNotFoundError:
        return inventario
