# model/libro.py
from model.base_datos.administrador_base_datos import Administrador_base_datos

class Libro:
    def __init__(self, idLibro, titulo, autor, precio, descuento, generos, calificacion, sinopsis, pdf_path=""):
        self.idLibro = idLibro
        self.titulo = titulo
        self.autor = autor
        self.precio = float(precio)
        self.descuento = float(descuento)
        self.generos = generos if isinstance(generos, list) else generos.split(",")
        self.calificacion = float(calificacion)
        self.sinopsis = sinopsis
        self.pdf_path = pdf_path

    def guardar_libro(self):
        """Guarda el libro en la base de datos."""
        db = Administrador_base_datos()
        db.create("libros", [
            self.idLibro, self.titulo, self.autor, self.precio, self.descuento,
            ",".join(self.generos), self.calificacion, self.sinopsis, self.pdf_path
        ])

    def __str__(self):
        return f"{self.titulo} de {self.autor} (${self.precio})"
