from model.biblioteca.libro import Libro
from model.base_datos.administrador_base_datos import Administrador_base_datos
from model.exceptions import BadRequestException

class Biblioteca:
    def __init__(self):
        self.db = Administrador_base_datos()
        self.libros = self.cargar_libros()

    def agregar_libro(self, libro):
        """Agrega un libro si no existe otro con el mismo ID."""
        if any(l.idLibro == libro.idLibro for l in self.libros):
            raise BadRequestException(f"El libro con ID {libro.idLibro} ya existe.")
        if not libro.titulo or not libro.autor:
            raise BadRequestException("El libro debe tener un título y un autor.")
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

    def buscar_libro_por_titulo(self, titulo):
        """Busca un libro por su título (sin distinguir mayúsculas o minúsculas)."""
        libro = next((libro for libro in self.libros if libro.titulo.lower() == titulo.lower()), None)
        if libro is None:
            raise BadRequestException(f"No se encontró un libro con el título {titulo}.")
        return libro

    def buscar_libros_por_genero(self, genero):
        """Devuelve una lista de libros que incluyan el género especificado."""
        return [libro for libro in self.libros if genero.lower() in [g.lower() for g in libro.generos]]
