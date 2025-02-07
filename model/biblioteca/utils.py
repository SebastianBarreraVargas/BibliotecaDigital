# model/utils.py
from PyPDF2 import PdfReader

def extraer_primera_pagina(pdf_path):
    try:
        with open(pdf_path, "rb") as pdf_file:
            reader = PdfReader(pdf_file)
            if len(reader.pages) > 0:
                first_page = reader.pages[0]
                text = first_page.extract_text()
                return text if text else "No se pudo extraer texto de la primera página."
            else:
                return "El PDF está vacío."
    except Exception as e:
        return f"Error al leer el PDF: {e}"
