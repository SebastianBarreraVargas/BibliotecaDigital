import csv
import os

USUARIOS_FILE = "./model/base_datos/usuarios.csv"
ADMINISTRADORES_FILE =  "./model/base_datos/usuarios.csv"
LIBROS_FILE =  "./model/base_datos/libros.csv"
CARPETA_PDFS = "pdfs_libros"

class Administrador_base_datos:
    def __init__(self):
        self.archivos = {
            "usuarios": USUARIOS_FILE,
            "administradores": ADMINISTRADORES_FILE,
            "libros": LIBROS_FILE
        }
        self.carpeta_pdfs = "pdfs_libros"
        self.ensure_files_and_folders_exist()


    def ensure_files_and_folders_exist(self):
        """Crea archivos CSV y carpeta si no existen."""
        if not os.path.exists(self.archivos["usuarios"]):
            with open(self.archivos["usuarios"], "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(["Nombre", "Email", "Password"])
        if not os.path.exists(self.archivos["administradores"]):
            with open(self.archivos["administradores"], "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(["Nombre", "Codigo", "Email", "Password"])
        if not os.path.exists(self.archivos["libros"]):
            with open(self.archivos["libros"], "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(["idLibro", "titulo", "autor", "precio", "descuento", "generos", "calificacion", "sinopsis",
                                 "pdf_path"])
        if not os.path.exists(self.carpeta_pdfs):
            os.makedirs(self.carpeta_pdfs)


    def create(self, tipo, data):
        """Crea un nuevo registro en el archivo indicado por 'tipo'."""
        if tipo not in self.archivos:
            print("Tipo de archivo no válido.")
            return

        with open(self.archivos[tipo], mode="a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(data)


    def read(self, tipo):
        """Lee y devuelve todos los registros de un archivo en formato de diccionarios."""
        if tipo not in self.archivos:
            print("Tipo de archivo no válido.")
            return []

        with open(self.archivos[tipo], mode="r", newline="") as f:
            reader = csv.DictReader(f)
            return list(reader)


    def update(self, tipo, search_field, search_value, update_data):
        """Actualiza un registro en el archivo indicado por 'tipo'."""
        if tipo not in self.archivos:
            print("Tipo de archivo no válido.")
            return

        rows = []
        updated = False

        with open(self.archivos[tipo], mode="r", newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row[search_field] == search_value:
                    row.update(update_data)
                    updated = True
                rows.append(row)

        if updated:
            with open(self.archivos[tipo], mode="w", newline="") as f:
                writer = csv.DictWriter(f, fieldnames=reader.fieldnames)
                writer.writeheader()
                writer.writerows(rows)
        else:
            print("Registro no encontrado.")


    def delete(self, tipo, search_field, search_value):
        """Elimina un registro en el archivo indicado por 'tipo'."""
        if tipo not in self.archivos:
            print("Tipo de archivo no válido.")
            return

        rows = []
        deleted = False

        with open(self.archivos[tipo], mode="r", newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row[search_field] != search_value:
                    rows.append(row)
                else:
                    deleted = True

        if deleted:
            with open(self.archivos[tipo], mode="w", newline="") as f:
                writer = csv.DictWriter(f, fieldnames=reader.fieldnames)
                writer.writeheader()
                writer.writerows(rows)
        else:
            print("Registro no encontrado.")