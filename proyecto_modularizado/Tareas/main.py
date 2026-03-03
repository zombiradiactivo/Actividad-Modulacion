# ── MENÚ / UI ────────────────────────────────────────────────

from tareas import Tareas


def menu():
    # Datos de prueba

    tareas = Tareas()

    tareas.agregar_tarea("Comprar leche")
    tareas.agregar_tarea("Estudiar Python")
    tareas.agregar_tarea("Hacer ejercicio")

    while True:
        print("\n╔══════════════════════════╗")
        print("║       TODO  LIST         ║")
        print("╠══════════════════════════╣")
        print("║ 1. Añadir tarea          ║")
        print("║ 2. Completar tarea       ║")
        print("║ 3. Eliminar tarea        ║")
        print("║ 4. Ver tareas            ║")
        print("║ 0. Salir                 ║")
        print("╚══════════════════════════╝")

        op = input("  Opción: ").strip()

        if op == "0":
            print("  👋 ¡Hasta luego!")
            break
        elif op == "1":
            desc    = input("  Descripción: ")
            _, msg  = tareas.agregar_tarea(desc)
            print(f"  {msg}")
        elif op == "2":
            id_str  = input("  ID de la tarea: ")
            _, msg  = tareas.completar_tarea(id_str)
            print(f"  {msg}")
        elif op == "3":
            id_str  = input("  ID a eliminar: ")
            _, msg  = tareas.eliminar_tarea(id_str)
            print(f"  {msg}")
        elif op == "4":
            tareas.listar_tareas()
        else:
            print("  ⚠️  Opción no válida.")

if __name__ == "__main__":
    menu()