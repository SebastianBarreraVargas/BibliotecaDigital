# controller.py
import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox
from model import Biblioteca, Libro, Login, Administrador, CARPETA_PDFS, extraer_primera_pagina

def seleccionar_pdf(entry_pdf):
    archivo_pdf = filedialog.askopenfilename(filetypes=[("Archivos PDF", "*.pdf")])
    if archivo_pdf:
        entry_pdf.delete(0, tk.END)
        entry_pdf.insert(0, archivo_pdf)

def registrar_usuario(nombre, email, password):
    usuario = Login(nombre, email, password)
    usuario.registrarUsuario()

def registrar_admin(nombre, codigo, email, password):
    admin = Administrador(nombre, codigo, email, password)
    admin.registrarAdministrador()

def eliminar_libro(root, libro, nombre_usuario):
    biblioteca = Biblioteca()
    try:
        biblioteca.borrar_libro(libro.idLibro)
        messagebox.showinfo("Éxito", f"El libro '{libro.titulo}' se ha eliminado correctamente.")
        from view import mostrar_moderacion_libros
        mostrar_moderacion_libros(root, nombre_usuario)
    except ValueError as e:
        messagebox.showerror("Error", str(e))

def agregar_libro(idLibro, titulo, autor, precio, descuento, generos, calificacion, sinopsis, pdf_path):
    biblioteca = Biblioteca()
    if not (idLibro and titulo and autor and precio and descuento and generos and calificacion and sinopsis):
        messagebox.showerror("Error", "Todos los campos son obligatorios.")
        return False
    try:
        precio = float(precio)
        descuento = float(descuento)
        calificacion = float(calificacion)
    except ValueError:
        messagebox.showerror("Error", "Precio, descuento y calificación deben ser valores numéricos.")
        return False
    nuevo_pdf_path = ""
    if pdf_path:
        nombre_pdf = f"{idLibro}_{os.path.basename(pdf_path)}"
        nuevo_pdf_path = os.path.join(CARPETA_PDFS, nombre_pdf)
        shutil.copy(pdf_path, nuevo_pdf_path)
    nuevo_libro = Libro(idLibro, titulo, autor, precio, descuento, generos, calificacion, sinopsis, nuevo_pdf_path)
    try:
        biblioteca.agregar_libro(nuevo_libro)
        messagebox.showinfo("Éxito", "Libro agregado correctamente.")
        return True
    except ValueError as e:
        messagebox.showerror("Error", str(e))
        return False

def buscar_libro(titulo):
    biblioteca = Biblioteca()
    libro = biblioteca.buscar_libro_por_titulo(titulo)
    return libro

def iniciar_sesion(email, password):
    usuario = Login("", email, password)
    return usuario.iniciarSesion()

def iniciar_sesion_admin(email, password):
    admin = Administrador("", "", email, password)
    return admin.iniciarSesion()
