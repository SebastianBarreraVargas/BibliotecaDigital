from model import Login
from tkinter import messagebox

class Administrador(Login):
    def __init__(self, nombre, codigo_trabajador, email, password):
        super().__init__(nombre, email, password)
        self.codigo_trabajador = codigo_trabajador

    def email_existe(self):
        administradores = self.db.read("administradores")
        return any(admin["Email"] == self.email for admin in administradores)

    def registrarAdministrador(self):
        error = self.validar_password(self.password)
        if error:
            messagebox.showerror("Error de Contraseña", error)
            return
        if self.email_existe():
            messagebox.showerror("Error", "El email ya está registrado como administrador.")
            return
        self.db.create("administradores", [self.nombre, self.codigo_trabajador, self.email, self.password])
        messagebox.showinfo("Registro Exitoso", "Administrador registrado correctamente.")

    def iniciarSesion(self):
        administradores = self.db.read("administradores")
        for admin in administradores:
            if admin["Email"] == self.email and admin["Password"] == self.password:
                messagebox.showinfo("Login Exitoso", f"Bienvenido {admin['Nombre']}")
                return True
        messagebox.showerror("Error", "Email o contraseña incorrectos.")
        return False