# model/libro.py
import os
import csv
from model.base import LIBROS_FILE

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
        self.pdf_path = pdf_path  # Ruta del PDF

    def guardar_libro(self):
        file_exists = os.path.exists(LIBROS_FILE)
        with open(LIBROS_FILE, "a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            if not file_exists:
                writer.writerow(["idLibro", "titulo", "autor", "precio", "descuento", "generos", "calificacion", "sinopsis", "pdf_path"])
            writer.writerow([
                self.idLibro, self.titulo, self.autor, self.precio, self.descuento,
                ",".join(self.generos), self.calificacion, self.sinopsis, self.pdf_path
            ])

    def __str__(self):
        return f"{self.titulo} de {self.autor} (${self.precio})"

class Biblioteca:
    def __init__(self):
        # Carga los libros del CSV al iniciar
        self.libros = self.cargar_libros()

    def agregar_libro(self, libro):
        """Agrega un libro si no existe otro con el mismo ID."""
        for l in self.libros:
            if l.idLibro == libro.idLibro:
                raise ValueError(f"El libro con ID {libro.idLibro} ya existe.")
        self.libros.append(libro)
        libro.guardar_libro()

    @staticmethod
    def cargar_libros():
        """Carga los libros del CSV."""
        libros = []
        if not os.path.exists(LIBROS_FILE):
            return libros

        with open(LIBROS_FILE, "r", newline="", encoding="utf-8") as f:
            reader = csv.reader(f)
            next(reader, None)  # Saltar la cabecera
            for row in reader:
                if len(row) < 9:
                    continue
                idLibro, titulo, autor, precio, descuento, generos, calificacion, sinopsis, pdf_path = row
                libros.append(Libro(idLibro, titulo, autor, precio, descuento, generos, calificacion, sinopsis, pdf_path))
        return libros

    def buscar_libro_por_titulo(self, titulo):
        """Busca un libro por su título (sin distinguir mayúsculas o minúsculas)."""
        for libro in self.libros:
            if libro.titulo.lower() == titulo.lower():
                return libro
        return None

    def buscar_libros_por_genero(self, genero):
        """Devuelve una lista de libros que incluyan el género especificado."""
        return [libro for libro in self.libros if genero.lower() in [g.lower() for g in libro.generos]]
