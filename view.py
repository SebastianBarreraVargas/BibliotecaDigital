# view.py
import os
import tkinter as tk
from tkinter import messagebox
from controller import (registrar_usuario, registrar_admin, seleccionar_pdf, agregar_libro,
                        buscar_libro, iniciar_sesion, iniciar_sesion_admin)
from model import Libro, Biblioteca, Login, Administrador, extraer_primera_pagina

# Variables globales para los widgets (estas variables se pueden encapsular en clases en una mejora futura)
entry_nombre = None
entry_email = None
entry_password = None
entry_codigo = None
entry_user = None
entry_pass = None
entry_idLibro = None
entry_titulo = None
entry_autor = None
entry_precio = None
entry_descuento = None
entry_generos = None
entry_calificacion = None
entry_sinopsis = None
entry_pdf_path = None
txt_area = None

def mostrar_pantalla_principal(root):
    for widget in root.winfo_children():
        widget.destroy()
    
    header = tk.Frame(root, bg="#e77e3e", height=50)
    header.pack(fill=tk.X)
    header_label = tk.Label(header, text="Biblioteca OnLine", font=("Arial", 18, "bold"), bg="#e77e3e", fg="black")
    header_label.pack(side=tk.LEFT, padx=10, pady=10)
    
    main_frame = tk.Frame(root, bg="white")
    main_frame.pack(pady=20)
    
    image_label = tk.Label(main_frame, text="📚\nTu Biblioteca Virtual", font=("Arial", 14), bg="#ddd", padx=50, pady=30)
    image_label.pack()
    
    btn_frame = tk.Frame(root, bg="white")
    btn_frame.pack(pady=10)
    
    btn_login = tk.Button(btn_frame, text="Login", font=("Arial", 12, "bold"),
                          bg="#0d1b2a", fg="white", width=15,
                          command=lambda: mostrar_login(root))
    btn_login.grid(row=0, column=0, padx=10)
    
    btn_login_admin = tk.Button(btn_frame, text="Login Admin", font=("Arial", 12, "bold"),
                                bg="#0d1b2a", fg="white", width=15,
                                command=lambda: mostrar_login_admin(root))
    btn_login_admin.grid(row=0, column=1, padx=10)
    
    btn_crear_cuenta = tk.Button(btn_frame, text="Crear Cuenta", font=("Arial", 12, "bold"),
                                 bg="#0d1b2a", fg="white", width=15,
                                 command=lambda: mostrar_registro(root))
    btn_crear_cuenta.grid(row=1, column=0, padx=5, pady=5)
    
    btn_crear_admin = tk.Button(btn_frame, text="Crear Cuenta Admin", font=("Arial", 12, "bold"),
                                bg="#0d1b2a", fg="white", width=15,
                                command=lambda: mostrar_registro_admin(root))
    btn_crear_admin.grid(row=1, column=1, padx=5, pady=5)

def mostrar_login(root):
    global entry_user, entry_pass
    for widget in root.winfo_children():
        widget.destroy()
    
    header = tk.Frame(root, bg="#e77e3e", height=50)
    header.pack(fill=tk.X)
    header_label = tk.Label(header, text="Biblioteca OnLine", font=("Arial", 18, "bold"),
                             bg="#e77e3e", fg="black")
    header_label.pack(side=tk.LEFT, padx=10, pady=10)
    header_label.bind("<Button-1>", lambda e: mostrar_pantalla_principal(root))
    
    main_frame = tk.Frame(root, bg="white")
    main_frame.pack(pady=20)
    
    tk.Label(main_frame, text="Email", font=("Arial", 12), bg="white").grid(row=0, column=0, pady=5, padx=10, sticky="w")
    entry_user = tk.Entry(main_frame, font=("Arial", 12), width=30)
    entry_user.grid(row=0, column=1, pady=5, padx=10)
    
    tk.Label(main_frame, text="Contraseña", font=("Arial", 12), bg="white").grid(row=1, column=0, pady=5, padx=10, sticky="w")
    entry_pass = tk.Entry(main_frame, font=("Arial", 12), width=30, show="*")
    entry_pass.grid(row=1, column=1, pady=5, padx=10)
    
    login_btn = tk.Button(main_frame, text="Login Usuario", font=("Arial", 12, "bold"),
                          bg="#0d1b2a", fg="white", width=20,
                          command=lambda: _iniciar_sesion(root))
    login_btn.grid(row=2, column=1, pady=10)

def _iniciar_sesion(root):
    global entry_user, entry_pass
    email = entry_user.get()
    password = entry_pass.get()
    nombre = iniciar_sesion(email, password)
    if nombre:
        mostrar_pantalla_usuario(root, nombre)

def mostrar_login_admin(root):
    global entry_user, entry_pass
    for widget in root.winfo_children():
        widget.destroy()
    
    header = tk.Frame(root, bg="#e77e3e", height=50)
    header.pack(fill=tk.X)
    header_label = tk.Label(header, text="Biblioteca OnLine", font=("Arial", 18, "bold"),
                             bg="#e77e3e", fg="black")
    header_label.pack(side=tk.LEFT, padx=10, pady=10)
    header_label.bind("<Button-1>", lambda e: mostrar_pantalla_principal(root))
    
    main_frame = tk.Frame(root, bg="white")
    main_frame.pack(pady=20)
    
    tk.Label(main_frame, text="Email", font=("Arial", 12), bg="white").grid(row=0, column=0, pady=5, padx=10, sticky="w")
    entry_user = tk.Entry(main_frame, font=("Arial", 12), width=30)
    entry_user.grid(row=0, column=1, pady=5, padx=10)
    
    tk.Label(main_frame, text="Contraseña", font=("Arial", 12), bg="white").grid(row=1, column=0, pady=5, padx=10, sticky="w")
    entry_pass = tk.Entry(main_frame, font=("Arial", 12), width=30, show="*")
    entry_pass.grid(row=1, column=1, pady=5, padx=10)
    
    login_btn = tk.Button(main_frame, text="Login Admin", font=("Arial", 12, "bold"),
                          bg="#0d1b2a", fg="white", width=20,
                          command=lambda: _iniciar_sesion_admin(root))
    login_btn.grid(row=2, column=1, pady=10)

def _iniciar_sesion_admin(root):
    global entry_user, entry_pass
    email = entry_user.get()
    password = entry_pass.get()
    if iniciar_sesion_admin(email, password):
        mostrar_pantalla_administrador(root, email)

def mostrar_registro(root):
    global entry_nombre, entry_email, entry_password
    for widget in root.winfo_children():
        widget.destroy()
    
    header = tk.Frame(root, bg="#e77e3e", height=50)
    header.pack(fill=tk.X)
    header_label = tk.Label(header, text="Biblioteca OnLine", font=("Arial", 18, "bold"),
                             bg="#e77e3e", fg="black")
    header_label.pack(pady=10)
    header_label.bind("<Button-1>", lambda e: mostrar_pantalla_principal(root))
    
    main_frame = tk.Frame(root, bg="white")
    main_frame.pack(pady=20)
    
    tk.Label(main_frame, text="Nombre", font=("Arial", 12), bg="white").grid(row=0, column=0, pady=5, padx=10, sticky="w")
    entry_nombre = tk.Entry(main_frame, font=("Arial", 12), width=30)
    entry_nombre.grid(row=0, column=1, pady=5, padx=10)
    
    tk.Label(main_frame, text="Email", font=("Arial", 12), bg="white").grid(row=1, column=0, pady=5, padx=10, sticky="w")
    entry_email = tk.Entry(main_frame, font=("Arial", 12), width=30)
    entry_email.grid(row=1, column=1, pady=5, padx=10)
    
    tk.Label(main_frame, text="Contraseña", font=("Arial", 12), bg="white").grid(row=2, column=0, pady=5, padx=10, sticky="w")
    entry_password = tk.Entry(main_frame, font=("Arial", 12), width=30, show="*")
    entry_password.grid(row=2, column=1, pady=5, padx=10)
    
    registrar_btn = tk.Button(main_frame, text="Registrar", font=("Arial", 12, "bold"),
                               bg="#0d1b2a", fg="white", width=15,
                               command=lambda: registrar_usuario(entry_nombre.get(), entry_email.get(), entry_password.get()))
    registrar_btn.grid(row=3, column=1, pady=10)

def mostrar_registro_admin(root):
    global entry_nombre, entry_email, entry_password, entry_codigo
    for widget in root.winfo_children():
        widget.destroy()
    
    header = tk.Frame(root, bg="#e77e3e", height=50)
    header.pack(fill=tk.X)
    header_label = tk.Label(header, text="Biblioteca OnLine", font=("Arial", 18, "bold"),
                             bg="#e77e3e", fg="black")
    header_label.pack(pady=10)
    header_label.bind("<Button-1>", lambda e: mostrar_pantalla_principal(root))
    
    main_frame = tk.Frame(root, bg="white")
    main_frame.pack(pady=20)
    
    tk.Label(main_frame, text="Nombre de Usuario", font=("Arial", 12), bg="white").grid(row=0, column=0, pady=5, padx=10, sticky="w")
    entry_nombre = tk.Entry(main_frame, font=("Arial", 12), width=30)
    entry_nombre.grid(row=0, column=1, pady=5, padx=10)
    
    tk.Label(main_frame, text="Correo electronico", font=("Arial", 12), bg="white").grid(row=1, column=0, pady=5, padx=10, sticky="w")
    entry_email = tk.Entry(main_frame, font=("Arial", 12), width=30)
    entry_email.grid(row=1, column=1, pady=5, padx=10)
    
    tk.Label(main_frame, text="Codigo Trabajador", font=("Arial", 12), bg="white").grid(row=2, column=0, pady=5, padx=10, sticky="w")
    entry_codigo = tk.Entry(main_frame, font=("Arial", 12), width=30)
    entry_codigo.grid(row=2, column=1, pady=5, padx=10)
    
    tk.Label(main_frame, text="Contraseña", font=("Arial", 12), bg="white").grid(row=3, column=0, pady=5, padx=10, sticky="w")
    entry_password = tk.Entry(main_frame, font=("Arial", 12), width=30, show="*")
    entry_password.grid(row=3, column=1, pady=5, padx=10)
    
    registrar_admin_btn = tk.Button(main_frame, text="Crear Cuenta Admin", font=("Arial", 12, "bold"),
                                    bg="#0d1b2a", fg="white", width=20,
                                    command=lambda: registrar_admin(entry_nombre.get(), entry_codigo.get(), entry_email.get(), entry_password.get()))
    registrar_admin_btn.grid(row=4, column=1, pady=10)

def mostrar_subir_libro(root):
    global entry_idLibro, entry_titulo, entry_autor, entry_precio, entry_descuento, entry_generos, entry_calificacion, entry_sinopsis, entry_pdf_path
    for widget in root.winfo_children():
        widget.destroy()
    
    header = tk.Frame(root, bg="#e77e3e", height=50)
    header.pack(fill=tk.X)
    header_label = tk.Label(header, text="Subir Libro", font=("Arial", 18, "bold"), bg="#e77e3e", fg="black")
    header_label.pack(pady=10)
    
    main_frame = tk.Frame(root, bg="white")
    main_frame.pack(pady=20)
    
    tk.Label(main_frame, text="ID Libro:", font=("Arial", 12), bg="white").grid(row=0, column=0, pady=5, padx=10, sticky="w")
    entry_idLibro = tk.Entry(main_frame, font=("Arial", 12), width=30)
    entry_idLibro.grid(row=0, column=1, pady=5, padx=10)
    
    tk.Label(main_frame, text="Título:", font=("Arial", 12), bg="white").grid(row=1, column=0, pady=5, padx=10, sticky="w")
    entry_titulo = tk.Entry(main_frame, font=("Arial", 12), width=30)
    entry_titulo.grid(row=1, column=1, pady=5, padx=10)
    
    tk.Label(main_frame, text="Autor:", font=("Arial", 12), bg="white").grid(row=2, column=0, pady=5, padx=10, sticky="w")
    entry_autor = tk.Entry(main_frame, font=("Arial", 12), width=30)
    entry_autor.grid(row=2, column=1, pady=5, padx=10)
    
    tk.Label(main_frame, text="Precio:", font=("Arial", 12), bg="white").grid(row=3, column=0, pady=5, padx=10, sticky="w")
    entry_precio = tk.Entry(main_frame, font=("Arial", 12), width=30)
    entry_precio.grid(row=3, column=1, pady=5, padx=10)
    
    tk.Label(main_frame, text="Descuento (%):", font=("Arial", 12), bg="white").grid(row=4, column=0, pady=5, padx=10, sticky="w")
    entry_descuento = tk.Entry(main_frame, font=("Arial", 12), width=30)
    entry_descuento.grid(row=4, column=1, pady=5, padx=10)
    
    tk.Label(main_frame, text="Géneros (separados por comas):", font=("Arial", 12), bg="white").grid(row=5, column=0, pady=5, padx=10, sticky="w")
    entry_generos = tk.Entry(main_frame, font=("Arial", 12), width=30)
    entry_generos.grid(row=5, column=1, pady=5, padx=10)
    
    tk.Label(main_frame, text="Calificación:", font=("Arial", 12), bg="white").grid(row=6, column=0, pady=5, padx=10, sticky="w")
    entry_calificacion = tk.Entry(main_frame, font=("Arial", 12), width=30)
    entry_calificacion.grid(row=6, column=1, pady=5, padx=10)
    
    tk.Label(main_frame, text="Sinopsis:", font=("Arial", 12), bg="white").grid(row=7, column=0, pady=5, padx=10, sticky="w")
    entry_sinopsis = tk.Entry(main_frame, font=("Arial", 12), width=30)
    entry_sinopsis.grid(row=7, column=1, pady=5, padx=10)
    
    entry_pdf_path = tk.Entry(main_frame, font=("Arial", 12), width=30)
    entry_pdf_path.grid(row=8, column=1, pady=5, padx=10)
    btn_seleccionar_pdf = tk.Button(main_frame, text="Seleccionar PDF", command=lambda: seleccionar_pdf(entry_pdf_path))
    btn_seleccionar_pdf.grid(row=8, column=2, padx=10)
    
    btn_agregar_libro = tk.Button(main_frame, text="Agregar Libro a la Biblioteca", font=("Arial", 12, "bold"),
                                  bg="#0d1b2a", fg="white", width=30,
                                  command=lambda: _agregar_libro(root))
    btn_agregar_libro.grid(row=9, column=1, pady=10)
    
    btn_volver = tk.Button(main_frame, text="Volver", font=("Arial", 12, "bold"),
                           bg="#d9534f", fg="white", width=15,
                           command=lambda: mostrar_pantalla_administrador(root, "Administrador"))
    btn_volver.grid(row=10, column=1, pady=10)

def _agregar_libro(root):
    global entry_idLibro, entry_titulo, entry_autor, entry_precio, entry_descuento, entry_generos, entry_calificacion, entry_sinopsis, entry_pdf_path
    generos = entry_generos.get().split(",")
    success = agregar_libro(entry_idLibro.get(), entry_titulo.get(), entry_autor.get(), entry_precio.get(),
                            entry_descuento.get(), generos, entry_calificacion.get(), entry_sinopsis.get(), entry_pdf_path.get())
    if success:
        mostrar_pantalla_administrador(root, "Administrador")

def mostrar_pantalla_usuario(root, nombre_usuario):
    global txt_area
    for widget in root.winfo_children():
        widget.destroy()
    
    header = tk.Frame(root, bg="#e77e3e", height=50)
    header.pack(fill=tk.X)
    header_label = tk.Label(header, text="Biblioteca OnLine", font=("Arial", 18, "bold"),
                             bg="#e77e3e", fg="black")
    header_label.pack(side=tk.LEFT, padx=10, pady=10)
    
    usuario_label = tk.Label(header, text=f"Bienvenido, {nombre_usuario}", font=("Arial", 12),
                             bg="#e77e3e", fg="white")
    usuario_label.pack(side=tk.RIGHT, padx=10, pady=10)
    
    main_frame = tk.Frame(root, bg="white")
    main_frame.pack(pady=20)
    
    txt_area = tk.Text(main_frame, height=1, width=20, font=("Arial", 12))
    txt_area.pack(pady=10)
    
    btn_buscar_libro = tk.Button(main_frame, text="Buscar Libro", font=("Arial", 12, "bold"),
                                 bg="#0d1b2a", fg="white", width=20,
                                 command=lambda: _buscar_libro(root))
    btn_buscar_libro.pack(pady=10)
    
    btn_buqueda_avanzada = tk.Button(main_frame, text="Busqueda Avanzada", font=("Arial", 12, "bold"),
                                    bg="#0d1b2a", fg="white", width=20)
    btn_buqueda_avanzada.pack(pady=10)
    
    btn_ver_libros = tk.Button(main_frame, text="Ver Mis Libros", font=("Arial", 12, "bold"),
                              bg="#0d1b2a", fg="white", width=20)
    btn_ver_libros.pack(pady=10)
    
    btn_cerrar_sesion = tk.Button(main_frame, text="Cerrar Sesión", font=("Arial", 12, "bold"),
                                  bg="#0d1b2a", fg="white", width=20,
                                  command=lambda: mostrar_pantalla_principal(root))
    btn_cerrar_sesion.pack(pady=10)

def _buscar_libro(root):
    global txt_area
    titulo = txt_area.get("1.0", tk.END).strip()
    libro = buscar_libro(titulo)
    if libro:
        mostrar_detalle_libro(root, libro)
    else:
        messagebox.showerror("No encontrado", "El libro no se encuentra en la base de datos.")

def mostrar_detalle_libro(root, libro):
    for widget in root.winfo_children():
        widget.destroy()
    
    header = tk.Frame(root, bg="#e77e3e", height=50)
    header.pack(fill=tk.X)
    header_label = tk.Label(header, text="Detalle del Libro", font=("Arial", 18, "bold"),
                             bg="#e77e3e", fg="black")
    header_label.pack(pady=10)
    
    main_frame = tk.Frame(root, bg="white")
    main_frame.pack(pady=20, fill=tk.BOTH, expand=True)
    
    panel_izquierdo = tk.Frame(main_frame, bg="white")
    panel_izquierdo.pack(side=tk.LEFT, padx=10, fill=tk.Y)
    
    tk.Label(panel_izquierdo, text=f"Título: {libro.titulo}", font=("Arial", 14, "bold"),
             bg="white").pack(pady=5, anchor="w")
    tk.Label(panel_izquierdo, text=f"Precio: ${libro.precio}", font=("Arial", 12),
             bg="white").pack(pady=5, anchor="w")
    tk.Label(panel_izquierdo, text=f"Autor: {libro.autor}", font=("Arial", 12),
             bg="white").pack(pady=5, anchor="w")
    
    panel_derecho = tk.Frame(main_frame, bg="white")
    panel_derecho.pack(side=tk.RIGHT, padx=10, fill=tk.BOTH, expand=True)
    
    if libro.pdf_path and os.path.exists(libro.pdf_path):
        texto_pdf = extraer_primera_pagina(libro.pdf_path)
    else:
        texto_pdf = "No hay PDF disponible."
    texto_widget = tk.Text(panel_derecho, height=20, width=40, font=("Arial", 10))
    texto_widget.insert(tk.END, texto_pdf)
    texto_widget.config(state=tk.DISABLED)
    texto_widget.pack(pady=10, fill=tk.BOTH, expand=True)
    
    btn_volver = tk.Button(root, text="Volver", font=("Arial", 12, "bold"),
                           bg="#d9534f", fg="white", width=15,
                           command=lambda: mostrar_pantalla_usuario(root, "Usuario"))
    btn_volver.pack(pady=10)

def mostrar_pantalla_administrador(root, nombre_usuario):
    for widget in root.winfo_children():
        widget.destroy()
    
    header = tk.Frame(root, bg="#e77e3e", height=50)
    header.pack(fill=tk.X)
    header_label = tk.Label(header, text="Biblioteca OnLine", font=("Arial", 18, "bold"),
                             bg="#e77e3e", fg="black")
    header_label.pack(side=tk.LEFT, padx=10, pady=10)
    
    usuario_label = tk.Label(header, text=f"Bienvenido, {nombre_usuario}", font=("Arial", 12),
                             bg="#e77e3e", fg="white")
    usuario_label.pack(side=tk.RIGHT, padx=10, pady=10)
    
    main_frame = tk.Frame(root, bg="white")
    main_frame.pack(pady=20)
    
    btn_subir_libro = tk.Button(main_frame, text="Subir Libro", font=("Arial", 12, "bold"),
                                bg="#0d1b2a", fg="white", width=20,
                                command=lambda: mostrar_subir_libro(root))
    btn_subir_libro.pack(pady=10)
    
    btn_moderar_libros = tk.Button(main_frame, text="Moderar Libros", font=("Arial", 12, "bold"),
                                   bg="#0d1b2a", fg="white", width=20)
    btn_moderar_libros.pack(pady=10)
    
    btn_cerrar_sesion = tk.Button(main_frame, text="Cerrar Sesión", font=("Arial", 12, "bold"),
                                  bg="#0d1b2a", fg="white", width=20,
                                  command=lambda: mostrar_pantalla_principal(root))
    btn_cerrar_sesion.pack(pady=10)
