import misfunciones as fun
from colorama import init, Fore, Style
import os
init(autoreset=True)

#base creada
fun.crear_base()

#tabla creada
fun.crear_tabla()


# Menú principal
while True:
        opcion = fun.menu()
        
        if opcion == "1":
            fun.registrar_producto()
        elif opcion == "2":
            fun.mostrar_productos()
        elif opcion == "3":
            fun.actualizar_stock()
        elif opcion == "4":
            fun.eliminar_producto()
        elif opcion == "5":
            fun.buscar_producto_por_id()
        elif opcion == "6":
            fun.reporte_bajo_stock()
        elif opcion == "0":
            fun.despedida()
            break
        else:
            print(Fore.RED + "⚠ Opción no válida, intente nuevamente." + Style.RESET_ALL)

        input(Fore.MAGENTA + "\nPresione ENTER para continuar..." + Style.RESET_ALL)
        os.system('cls' if os.name == 'nt' else 'clear')
        #os.system('cls' if os.name == 'nt' else 'clear')