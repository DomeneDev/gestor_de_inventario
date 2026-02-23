📦 Gestor de Inventario Pro
Este es un proyecto modular en Python diseñado para administrar el catálogo de productos de un almacén mediante el uso de estructuras de datos anidadas. El proyecto está enfocado en aplicar buenas prácticas de desarrollo, tipado estático y la gestión eficiente de flujos de stock.

🚀 Características
Gestión Inteligente de Stock: Registro de nuevos productos y actualización automática de existencias y precios.

Control de Transacciones: Sistema de validación de ventas que impide operaciones sin stock suficiente.

Valoración de Activos:

Cálculo del valor total monetario del inventario.

Redondeo de precisión para métricas financieras.

Soporte para múltiples tipos de datos (str, int, float).

📂 Estructura del Proyecto
La arquitectura del código sigue el principio de separación de responsabilidades:

```plaintext
gestor_inventario/
├── main.py # Interfaz de usuario y orquestación del programa.
├── inventario_logic.py # Núcleo lógico (motor de gestión de productos).
└── README.md # Documentación del proyecto.
```
🛠️ Instalación y Uso
Clona este repositorio o descarga los archivos.

Asegúrate de tener instalado Python 3.9 o superior.

Ejecuta el programa principal:

Bash

python main.py

📝 Ejemplo de Salida

```plaintext

Introduce el producto a añadir: Manzana
Introduce el precio: 0.50
Introduce la cantidad: 10

Estado del Inventario:
- Manzana: 10 unidades a 0.5€/u.
Estadísticas:
{
'total_productos_distintos': 1,
'valor_total_stock': 5.0,
'stock_total_unidades': 10
}
```

🛡️ Roadmap de Aprendizaje
Este proyecto evolucionará conforme avance mi formación en Python siguiendo ciclos de mejora continua:

[x] Sprint 1: Lógica core y diccionarios anidados .

[x] Sprint 2: Implementación de manejo de excepciones (productos no encontrados).

[x] Sprint 3: Refactorización Arquitectónica (Utils).

[x] Sprint 4: Persistencia de datos en archivos .csv (Base de datos local)(Estado actual).

[ ] Sprint 5: Refactorización a Programación Orientada a Objetos (Clase Producto y Almacén).
