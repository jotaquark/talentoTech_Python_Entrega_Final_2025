import sqlite3
from colorama import init, Fore, Style , Back
import time

init(autoreset=True)

# Conexión a la base de datos
def obtener_conexion():
    return sqlite3.connect("inventario.db")

# Crear base de datos
def crear_base():
    conexion = sqlite3.connect("inventario.db")
    print(Fore.GREEN + "Conexion Exitosa" + Style.RESET_ALL)
    conexion.close()

# Crear tabla productos
def crear_tabla():
    conn = obtener_conexion()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            descripcion TEXT,
            cantidad INTEGER NOT NULL,
            precio REAL NOT NULL,
            categoria TEXT
        );
    """)
    conn.commit()
    conn.close()
#tabla creada explicacion:
# La tabla "productos" tiene los siguientes campos:
# - id: Identificador único del producto (clave primaria).  
# - nombre: Nombre del producto (no puede ser nulo).
# - descripcion: Descripción del producto (opcional).
# - cantidad: Cantidad disponible del producto (no puede ser nulo).
# - precio: Precio del producto (no puede ser nulo).
# - categoria: Categoría del producto (opcional).   

# Menú de opciones
def menu():
    print(Fore.CYAN + "=" * 60)
    print(Fore.CYAN + "         SISTEMA DE INVENTARIO - CARREFOUR")
    print(Fore.CYAN + "=" * 60)

    print(Fore.GREEN + "[1]" + Style.RESET_ALL + " Registrar nuevo producto")
    print(Fore.GREEN + "[2]" + Style.RESET_ALL + " Ver todos los productos")
    print(Fore.GREEN + "[3]" + Style.RESET_ALL + " Actualizar cantidad de un producto")
    print(Fore.GREEN + "[4]" + Style.RESET_ALL + " Eliminar un producto")
    print(Fore.GREEN + "[5]" + Style.RESET_ALL + " Buscar producto por ID")
    print(Fore.GREEN + "[6]" + Style.RESET_ALL + " Reporte de productos con bajo stock")
    print(Fore.GREEN + "[0]" + Style.RESET_ALL + " Salir\n")
    opcion = input(Fore.YELLOW + "Seleccione una opción: " + Style.RESET_ALL)
    return (opcion)

# Función para mostrar filas de productos
def mostrar_filas(filas):
    print(Fore.CYAN + "\n"+"-" * 80)
    print("ID | NOMBRE          | DESCRIPCIÓN     | CANTIDAD | PRECIO | CATEGORÍA")
    print(Fore.CYAN +"-" * 80 + Style.RESET_ALL)
    for fila in filas:
        id_, nombre, descripcion, stock, precio, categoria = fila
        print(Fore.CYAN + f"{id_:<3}| {nombre:<15} | {descripcion:<15} | {stock:<8} | {precio:<6} | {categoria}")

#------ Función de despedida
def despedida():
    print(Fore.CYAN + "=" * 60)
    print(Fore.CYAN + "   GRACIAS POR USAR EL SISTEMA DE INVENTARIO - CARREFOUR   ")
    print(Fore.CYAN + "=" * 60 + Style.RESET_ALL)
    time.sleep(0.8)
    mensaje = "Cerrando el sistema"
    # Animación de puntos suspensivos
    # mas puintos cada 0.5 segundos
    for i in range(6):
        puntos = "." * i
        print(Fore.YELLOW + f"\r{mensaje}{puntos}   ", end="", flush=True)
        time.sleep(0.5)
    print()  # salto de línea
    time.sleep(0.5)
    # “Cartel” de despedida
    print(
        Fore.BLACK + Back.GREEN +
        "\n   ✔ Sesión cerrada correctamente.                      " +
        Style.RESET_ALL
    )
    time.sleep(0.7)
    print(
        Fore.MAGENTA +
        "\n   🛒 ¡Hasta luego! Gracias por confiar en nuestro sistema.   \n"
        + Style.RESET_ALL
    )
    time.sleep(1.5)

#------ Función para ingresar datos con validación
def ingresodato(mensaje="texto",nulo=False,type=str):  
    dato = input(Fore.YELLOW + mensaje + Style.RESET_ALL).strip().capitalize()
    if nulo:
        while dato.strip().capitalize() == "":
            print(Fore.RED + "⚠ El campo no puede estar vacío. Intente nuevamente." + Style.RESET_ALL)
            dato = input(Fore.YELLOW + mensaje + Style.RESET_ALL).strip().capitalize()
    # Validación para tipos numéricos
    if type == int:
        while True:
            try:
                dato = int(dato)
                if dato < 0:
                    print(Fore.RED + "⚠ El valor no puede ser negativo. Intente nuevamente." + Style.RESET_ALL)
                    dato = input(Fore.YELLOW + mensaje + Style.RESET_ALL)
                    continue
                break
            except ValueError:
                print(Fore.RED + "⚠ Ingrese un número entero válido." + Style.RESET_ALL)
                dato = input(Fore.YELLOW + mensaje + Style.RESET_ALL)
    # Validación para tipos numéricos
    if type == float:
        while True:
            try:
                dato = float(dato)
                if dato < 0:
                    print(Fore.RED + "⚠ El valor no puede ser negativo. Intente nuevamente." + Style.RESET_ALL)
                    dato = input(Fore.YELLOW + mensaje + Style.RESET_ALL)
                    continue
                break
            except ValueError:
                print(Fore.RED + "⚠ Ingrese un número válido." + Style.RESET_ALL)
                dato = input(Fore.YELLOW + mensaje + Style.RESET_ALL)
    return dato

#------ Funciónes para el menu
# Registrar nuevo producto
#opcion 1
def registrar_producto():
    conn = obtener_conexion()
    cursor = conn.cursor()
    print(Fore.CYAN + "\n--- Registrar nuevo producto ---" + Style.RESET_ALL)
    nombre = ingresodato("Nombre: ",True)
    descripcion = ingresodato("Descripción (opcional): ",False)
    cantidad= ingresodato("Cantidad: ",True,int)
    precio= ingresodato("Precio: ",True,float)
    categoria= ingresodato("Categoría (opcional): ",False)

    cursor.execute("""
        INSERT INTO productos (nombre, descripcion, cantidad, precio, categoria)
        VALUES (?, ?, ?, ?, ?)
    """, (nombre, descripcion, cantidad, precio, categoria))

    conn.commit()
    conn.close()
    print(Fore.GREEN + "✅ Producto registrado correctamente." + Style.RESET_ALL)

# Ver todos los productos
#opcion 2
def mostrar_productos():
    conn = obtener_conexion()
    cursor = conn.cursor()

    cursor.execute("SELECT id, nombre, descripcion, cantidad, precio, categoria   FROM productos")
    filas = cursor.fetchall()
    conn.close()

    print(Fore.CYAN + "\n--- Lista de productos ---" + Style.RESET_ALL)
    if not filas:
        print(Fore.RED + "No hay productos cargados." + Style.RESET_ALL)
        return
    mostrar_filas(filas)

# Actualizar cantidad de un producto
#opcion 3
def actualizar_stock():
    conn = obtener_conexion()
    cursor = conn.cursor()

    print(Fore.CYAN + "\n--- Actualizar stock de producto ---" + Style.RESET_ALL)
    
    id_prod= ingresodato("ID del producto: ",True,int)
    nuevo_stock= ingresodato("Nuevo stock: ",True,int)  

    cursor.execute("SELECT id FROM productos WHERE id = ?", (id_prod,))
    #fetchone() devuelve None si no hay resultados
    if cursor.fetchone() is None:
        print(Fore.RED + "⚠ No existe un producto con ese ID." + Style.RESET_ALL)
        conn.close()
        return

    cursor.execute("""
        UPDATE productos
        SET cantidad = ?
        WHERE id = ?
    """, (nuevo_stock, id_prod))

    conn.commit()
    conn.close()
    print(Fore.GREEN + "✅ Stock actualizado correctamente." + Style.RESET_ALL)

# Eliminar un producto
#opcion 4
def eliminar_producto():
    conn = obtener_conexion()
    cursor = conn.cursor()

    print(Fore.CYAN + "\n--- Eliminar producto ---" + Style.RESET_ALL)
    id_prod = ingresodato("ID del producto a eliminar: ",True,int)

    cursor.execute("SELECT id FROM productos WHERE id = ?", (id_prod,))
    if cursor.fetchone() is None:
        print(Fore.RED + "⚠ No existe un producto con ese ID." + Style.RESET_ALL)
        conn.close()
        return

    cursor.execute("DELETE FROM productos WHERE id = ?", (id_prod,))

    conn.commit()
    conn.close()
    print(Fore.GREEN + "✅ Producto eliminado correctamente." + Style.RESET_ALL)

# Buscar producto por ID
#opcion 5
def buscar_producto_por_id():
    conn = obtener_conexion()
    cursor = conn.cursor()

    print(Fore.CYAN + "\n--- Buscar producto por ID ---" + Style.RESET_ALL)
    id_prod = ingresodato("ID del producto a buscar: ",True,int)

    cursor.execute("""
        SELECT id, nombre, descripcion, cantidad, precio, categoria
        FROM productos
        WHERE id = ?
    """, (id_prod,))
    fila = cursor.fetchall()
    conn.close()

    if fila is None:
        print(Fore.RED + "⚠ No se encontró un producto con ese ID." + Style.RESET_ALL)
        return

    print(Fore.CYAN + "\n--- Detalles del producto ---" + Style.RESET_ALL)
    mostrar_filas(fila)

# Reporte de productos con bajo stock
#opcion 6
def reporte_bajo_stock():
    conn = obtener_conexion()
    cursor = conn.cursor()
    print(Fore.CYAN + "\n--- Reporte de productos con bajo stock ---" + Style.RESET_ALL)
    limite = ingresodato("Ingrese el límite de stock: ",True,int)
    
    cursor.execute("""
        SELECT id, nombre, descripcion, cantidad, precio, categoria
        FROM productos
        WHERE cantidad <= ?
    """, (limite,))
    filas = cursor.fetchall()
    conn.close()

    if not filas:
        print(Fore.RED + "⚠ No hay productos con stock igual o inferior al límite especificado." + Style.RESET_ALL)
        return
    print(Fore.CYAN + "\n--- Productos con bajo stock ---" + Style.RESET_ALL)
    mostrar_filas(filas)
#------ Fin Funciónes para el menu