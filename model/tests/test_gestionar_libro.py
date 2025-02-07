import pytest
from model.biblioteca.biblioteca import Biblioteca, BadRequestException, NotAuthorizedException
from model.biblioteca.libro import Libro
from model.usuarios.usuario import Login
from model.base_datos.administrador_base_datos import Administrador_base_datos
from unittest.mock import MagicMock

@pytest.fixture
def mock_db():
    mock_db = MagicMock(spec=Administrador_base_datos)
    
    # Simulamos datos del CSV de libros
    mock_db.read.return_value = [
        {
            "idLibro": 1, "titulo": "Libro Existente", "autor": "Autor Existente",
            "precio": 15.0, "descuento": 5, "generos": ["Ficción"],
            "calificacion": 4.0, "sinopsis": "Sinopsis", "pdf_path": "pdfs_libros/libro.pdf"
        }
    ]
    return mock_db

@pytest.fixture
def biblioteca(mock_db):
    biblioteca = Biblioteca()
    biblioteca.db = mock_db  # Usamos el mock en vez de la base de datos real
    biblioteca.libros = biblioteca.cargar_libros()  # Cargar los datos simulados
    return biblioteca

@pytest.fixture
def libro_valido():
    return Libro(2, "El Gran Libro", "Autor Ejemplo", 20.5, 10, ["Ficción"], 4.5, "Sinopsis del libro", "pdfs_libros/libro.pdf")

@pytest.fixture
def login_valido():
    return Login("Juan", "juan@example.com", "Contraseña123!")

def test_agregar_libro_duplicado(biblioteca, libro_valido):
    with pytest.raises(BadRequestException, match="El libro con ID 2 ya existe."):
        biblioteca.agregar_libro(libro_valido)

def test_agregar_libro_incompleto(biblioteca):
    libro_incompleto = Libro(3, "", "", 10.0, 0, ["Drama"], 3.0, "Sinopsis", "pdfs_libros/libro.pdf")
    with pytest.raises(BadRequestException, match="El libro debe tener un título y un autor."):
        biblioteca.agregar_libro(libro_incompleto)

def test_iniciar_sesion_incorrecto(mock_db, login_valido):
    login_valido.db = mock_db  # Inyectamos el mock de db en el objeto Login
    login_valido.email = "incorrecto@example.com"
    login_valido.password = "ContraseñaErronea"

    with pytest.raises(NotAuthorizedException, match="Email o contraseña incorrectos."):
        login_valido.iniciarSesion()
