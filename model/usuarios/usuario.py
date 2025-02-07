import re
from model.base_datos.administrador_base_datos import Administrador_base_datos
from tkinter import messagebox

class Login:
    def __init__(self, nombre, email, password):
        self.nombre = nombre
        self.email = email
        self.password = password
        self.db = Administrador_base_datos()

    def email_existe(self):
        usuarios = self.db.read("usuarios")
        return any(user["Email"] == self.email for user in usuarios)

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
            messagebox.showerror("Error de Contraseña", error)
            return
        if self.email_existe():
            messagebox.showerror("Error", "El email ya está registrado.")
            return
        self.db.create("usuarios", [self.nombre, self.email, self.password, "", ""])
        messagebox.showinfo("Registro Exitoso", "Usuario registrado correctamente.")

    def iniciarSesion(self):
        usuarios = self.db.read("usuarios")
        for user in usuarios:
            if user["Email"] == self.email and user["Password"] == self.password:
                messagebox.showinfo("Login Exitoso", f"Bienvenido {user['Nombre']}")
                return user["Nombre"]
        messagebox.showerror("Error", "Email o contraseña incorrectos.")
        return None
