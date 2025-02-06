# model/base.py
import os
import csv

# Constantes globales
USUARIOS_FILE = "usuarios.csv"
ADMINISTRADORES_FILE = "administradores.csv"
LIBROS_FILE = "libros.csv"
CARPETA_PDFS = "pdfs_libros"

def inicializar_archivos():
    if not os.path.exists(USUARIOS_FILE):
        with open(USUARIOS_FILE, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Nombre", "Email", "Password"])
    if not os.path.exists(ADMINISTRADORES_FILE):
        with open(ADMINISTRADORES_FILE, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Nombre", "Codigo", "Email", "Password"])
    if not os.path.exists(LIBROS_FILE):
        with open(LIBROS_FILE, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["idLibro", "titulo", "autor", "precio", "descuento", "generos", "calificacion", "sinopsis", "pdf_path"])
    if not os.path.exists(CARPETA_PDFS):
        os.makedirs(CARPETA_PDFS)

# Llamamos a la función para asegurarnos de que se creen los archivos cuando se importe el módulo.
inicializar_archivos()
