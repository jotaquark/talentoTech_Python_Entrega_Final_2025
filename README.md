# Sistema de Inventario (Proyecto Final)

Pequeña aplicación de consola en **Python** para gestionar el inventario de productos de un comercio.
Permite registrar productos, consultarlos, actualizarlos y eliminar registros usando una base de datos **SQLite** y una interfaz en consola coloreada con **colorama**.

## 🧩 Funcionalidades

* Crear automáticamente la base de datos `inventario.db` y la tabla `productos`.
* Menú interactivo en consola:

  1. Registrar nuevo producto
  2. Ver todos los productos
  3. Actualizar cantidad de un producto
  4. Eliminar un producto
  5. Buscar producto por ID
  6. Reporte de productos con bajo stock
  7. Salir del sistema
* Validación básica de datos de entrada (campos obligatorios, tipos numéricos, valores negativos, etc.).
* Mensajes en colores para mejorar la legibilidad (éxitos, errores, advertencias).

## 🏗 Tecnologías utilizadas

* **Python 3**
* **SQLite3** (módulo estándar `sqlite3`)
* **Colorama** para colores en la terminal

## 📂 Estructura del proyecto

```text
.
├── programa.py        # Punto de entrada de la aplicación (menú principal)
├── misfunciones.py    # Funciones de negocio y acceso a datos (CRUD y validaciones)
├── inventario.db      # Base de datos SQLite (se crea automáticamente si no existe)
└── __pycache__/       # Archivos compilados de Python
```

## 🗃 Modelo de datos

La tabla principal del sistema es `productos`:

```sql
CREATE TABLE IF NOT EXISTS productos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    descripcion TEXT,
    cantidad INTEGER NOT NULL,
    precio REAL NOT NULL,
    categoria TEXT
);
```

Campos:

* `id`: Identificador único del producto.
* `nombre`: Nombre del producto (obligatorio).
* `descripcion`: Descripción opcional del producto.
* `cantidad`: Stock disponible (entero, obligatorio).
* `precio`: Precio unitario del producto (real, obligatorio).
* `categoria`: Categoría del producto (opcional).

## ✅ Requisitos previos

* Python 3.10+ instalado
* Módulo `colorama` instalado

Puedes instalar `colorama` con:

```bash
pip install colorama
```

> 💡 SQLite viene incluido por defecto con Python mediante el módulo `sqlite3`, por lo que no hace falta instalar nada extra.

## 🚀 Cómo ejecutar el proyecto

1. Clonar este repositorio o descargar los archivos:

```bash
git clone https://github.com/<tu-usuario>/<tu-repo>.git
cd <tu-repo>
```

2. (Opcional) Crear y activar un entorno virtual:

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux / macOS
source venv/bin/activate
```

3. Instalar dependencias:

```bash
pip install colorama
```

4. Ejecutar el programa:

```bash
python programa.py
```

Al iniciar, el programa:

* Comprueba/crea la base de datos `inventario.db`.
* Comprueba/crea la tabla `productos`.
* Muestra el menú principal en consola.

## 🖥 Ejemplo de menú

```text
============================================================
         SISTEMA DE INVENTARIO - CARREFOUR
============================================================
[1] Registrar nuevo producto
[2] Ver todos los productos
[3] Actualizar cantidad de un producto
[4] Eliminar un producto
[5] Buscar producto por ID
[6] Reporte de productos con bajo stock
[0] Salir

Seleccione una opción:
```

## 🛣 Posibles mejoras futuras

* Manejo de productos inactivos / baja lógica en lugar de borrado físico.
* Exportar listados a CSV/Excel.
* Agregar filtros por categoría o rango de precios.
* Implementar pruebas automatizadas (unit tests).
* Crear una interfaz gráfica (por ejemplo, con Tkinter o una app web).

## 👤 Autor

Proyecto final desarrollado por **Juan José Rojas** (Jota).

Si quieres proponer mejoras o reportar errores, puedes abrir un *issue* o enviar un *pull request*.
