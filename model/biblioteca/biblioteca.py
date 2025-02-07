from model.biblioteca.libro import Libro
from model.base_datos.administrador_base_datos import Administrador_base_datos
import os

class Biblioteca:
    def __init__(self):
        self.db = Administrador_base_datos()
        self.libros = self.cargar_libros()

    def agregar_libro(self, libro):
        """Agrega un libro si no existe otro con el mismo ID."""
        if any(l.idLibro == libro.idLibro for l in self.libros):
            raise ValueError(f"El libro con ID {libro.idLibro} ya existe.")
        self.libros.append(libro)
        libro.guardar_libro()

    def cargar_libros(self):
        """Carga los libros desde la base de datos."""
        libros = []
        datos = self.db.read("libros")
        for row in datos:
            libros.append(
                Libro(
                    row["idLibro"], row["titulo"], row["autor"], row["precio"],
                    row["descuento"], row["generos"], row["calificacion"],
                    row["sinopsis"], row["pdf_path"]
                )
            )
        return libros
    
    def borrar_libro(self, idLibro):
        """Borra un libro de la base de datos, elimina el archivo PDF y lo quita de la lista en memoria."""
        # Buscar el libro a eliminar en la lista en memoria
        libro_a_eliminar = next((libro for libro in self.libros if libro.idLibro == idLibro), None)
        if libro_a_eliminar is None:
            raise ValueError(f"No se encontró un libro con ID {idLibro}.")

        # Eliminar el archivo PDF asociado, si existe
        if libro_a_eliminar.pdf_path and os.path.exists(libro_a_eliminar.pdf_path):
            try:
                os.remove(libro_a_eliminar.pdf_path)
            except Exception as e:
                raise ValueError(f"Error al eliminar el archivo PDF: {e}")

        # Eliminar el libro de la base de datos.
        # Se asume que el método delete tiene la firma: delete(tabla, columna, valor)
        self.db.delete("libros", "idLibro", idLibro)

        # Eliminar el libro de la lista en memoria
        self.libros.remove(libro_a_eliminar)

    def buscar_libro_por_titulo(self, titulo):
        """Busca un libro por su título (sin distinguir mayúsculas o minúsculas)."""
        return next((libro for libro in self.libros if libro.titulo.lower() == titulo.lower()), None)

    def buscar_libros_por_genero(self, genero):
        """Devuelve una lista de libros que incluyan el género especificado."""
        return [libro for libro in self.libros if genero.lower() in [g.lower() for g in libro.generos]]
