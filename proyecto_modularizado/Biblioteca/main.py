from biblioteca import Biblioteca
from datos_prueba import cargar_ejemplos


def mostrar_menu():
    print("""
=== MENÚ BIBLIOTECA ===
1. Prestar libro
2. Devolver libro
3. Comprar (Añadir stock)
4. Vender libro
5. Ver Catálogo
0. Salir
""")



def ejecutar_app():
    inventario = Biblioteca("Biblioteca Central")
    cargar_ejemplos(inventario)
    
    opciones = {
        "1": lambda: inventario.prestar_libro(input("Título: ")),
        "2": lambda: inventario.devolver_libro(input("Título: ")),
        "3": lambda: inventario.comprar_libro(
            input("Título: "), 
            input("Autor: "),
            float(input("Precio: ")), 
            int(input("Cantidad: "))
        ),
        "4": lambda: inventario.vender_libro(input("Título: ")),
        "5": inventario.mostrar_catalogo,
    }

    while True:
        mostrar_menu()
        op = input("Opción: ").strip()

        if op == "0":
            print("👋 ¡Hasta luego!")
            break
        elif op in opciones:
            opciones[op]()
        else:
            print("Opción inválida.")


if __name__ == "__main__":
    ejecutar_app()