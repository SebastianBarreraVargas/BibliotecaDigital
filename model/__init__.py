# model/__init__.py
from .base import USUARIOS_FILE, ADMINISTRADORES_FILE, LIBROS_FILE, CARPETA_PDFS, inicializar_archivos
from .libro import Libro, Biblioteca
from .usuario import Login, Administrador
from .utils import extraer_primera_pagina
