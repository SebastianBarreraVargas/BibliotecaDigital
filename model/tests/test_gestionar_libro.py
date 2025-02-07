import pytest
import os
from model.biblioteca.biblioteca import Biblioteca
from model.biblioteca.libro import Libro
from model.usuarios.usuario import Usuario
from model.exceptions import BadRequestException, NotAuthorizedException
from model.base_datos.administrador_base_datos import Administrador_base_datos

@pytest.fixture
def biblioteca():
    biblioteca = Biblioteca()
    biblioteca.db = Administrador_base_datos()
    biblioteca.libros = {
        1: Libro(123333, "Libro Existente", "Autor Existente", 15.0, 5, ["Ficción"], 4.0, "Sinopsis", "pdfs_libros/libro.pdf")
    } 
    return biblioteca

@pytest.fixture
def libro_valido():
    return Libro(9999, "El Gran Libro", "Autor Ejemplo", 20.5, 10, ["Ficción"], 4.5, "Sinopsis del libro", "pdfs_libros/libro.pdf")

@pytest.fixture
def login_valido():
    return Usuario("Juan", "juan@example.com", "Contraseña123!")

def test_agregar_libro_duplicado(biblioteca, libro_valido):
    biblioteca.agregar_libro(libro_valido)  
    with pytest.raises(BadRequestException, match="El libro con ID 9999 ya existe."):
        biblioteca.agregar_libro(libro_valido)  
    biblioteca.borrar_libro(libro_valido.idLibro)

def test_agregar_libro_incompleto(biblioteca):
    libro_incompleto = Libro(3, "", "", 10.0, 0, ["Drama"], 3.0, "Sinopsis", "pdfs_libros/libro.pdf")
    with pytest.raises(BadRequestException, match="El libro debe tener un título y un autor."):
        biblioteca.agregar_libro(libro_incompleto)

    if libro_incompleto.idLibro in biblioteca.libros:
        biblioteca.borrar_libro(libro_incompleto.idLibro)

def test_iniciar_sesion_incorrecto(login_valido):
    login_valido.email = "incorrecto@example.com"
    login_valido.password = "ContraseñaErronea"

    with pytest.raises(NotAuthorizedException, match="Email o contraseña incorrectos."):
        login_valido.iniciarSesion()
