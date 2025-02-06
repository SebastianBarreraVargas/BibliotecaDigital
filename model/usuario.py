# model/usuario.py
import os
import csv
import re
from model.base import USUARIOS_FILE, ADMINISTRADORES_FILE

class Login:
    def __init__(self, nombre, email, password):
        self.nombre = nombre
        self.email = email
        self.password = password

    def email_existe(self):
        with open(USUARIOS_FILE, "r", newline="") as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                if row[1] == self.email:
                    return True
        return False

    def validar_password(self, password):
        if len(password) < 8:
            return "La contraseña debe tener al menos 8 caracteres."
        if not any(char.isupper() for char in password):
            return "La contraseña debe contener al menos una letra mayúscula."
        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
            return "La contraseña debe contener al menos un carácter especial."
        return None

    def registrarUsuario(self):
        error = self.validar_password(self.password)
        if error:
            from tkinter import messagebox
            messagebox.showerror("Error de Contraseña", error)
            return
        if self.email_existe():
            from tkinter import messagebox
            messagebox.showerror("Error", "El email ya está registrado.")
            return
        with open(USUARIOS_FILE, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([self.nombre, self.email, self.password])
        from tkinter import messagebox
        messagebox.showinfo("Registro Exitoso", "Usuario registrado correctamente.")

    def iniciarSesion(self):
        with open(USUARIOS_FILE, "r", newline="") as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                if row[1] == self.email and row[2] == self.password:
                    from tkinter import messagebox
                    messagebox.showinfo("Login Exitoso", f"Bienvenido {row[0]}")
                    return row[0]
        from tkinter import messagebox
        messagebox.showerror("Error", "Email o contraseña incorrectos.")
        return None

class Administrador(Login):
    def __init__(self, nombre, codigo_trabajador, email, password):
        self.nombre = nombre
        self.codigo_trabajador = codigo_trabajador
        self.email = email
        self.password = password

    def email_existe(self):
        with open(ADMINISTRADORES_FILE, "r", newline="") as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                if row[2] == self.email:
                    return True
        return False

    def registrarAdministrador(self):
        error = self.validar_password(self.password)
        if error:
            from tkinter import messagebox
            messagebox.showerror("Error de Contraseña", error)
            return
        if self.email_existe():
            from tkinter import messagebox
            messagebox.showerror("Error", "El email ya está registrado como administrador.")
            return
        with open(ADMINISTRADORES_FILE, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([self.nombre, self.codigo_trabajador, self.email, self.password])
        from tkinter import messagebox
        messagebox.showinfo("Registro Exitoso", "Administrador registrado correctamente.")

    def iniciarSesion(self):
        with open(ADMINISTRADORES_FILE, "r", newline="") as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                if row[2] == self.email and row[3] == self.password:
                    from tkinter import messagebox
                    messagebox.showinfo("Login Exitoso", f"Bienvenido {row[0]}")
                    return True
        from tkinter import messagebox
        messagebox.showerror("Error", "Email o contraseña incorrectos.")
        return False
