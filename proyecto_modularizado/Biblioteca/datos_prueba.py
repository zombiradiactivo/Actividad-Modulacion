from models import Libro
from biblioteca import Biblioteca

def cargar_ejemplos(instancia_biblioteca: Biblioteca):
    """Carga una lista inicial de libros en la biblioteca proporcionada."""
    libros = [
        Libro("El Quijote", "Cervantes", 15.00, 3),
        Libro("Cien años", "García Márquez", 12.50, 2),
        Libro("1984", "Orwell", 10.00, 1)
    ]
    for l in libros:
        instancia_biblioteca.agregar_libro(l)