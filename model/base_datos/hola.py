import csv
import os
from pathlib import Path

direccion = Path('.')
USUARIOS_FILE = direccion / "usuarios.csv"
ADMINISTRADORES_FILE = direccion /"administradores.csv"
LIBROS_FILE = direccion / "libros.csv"
CARPETA_PDFS = "pdfs_libros"

print(USUARIOS_FILE)