import pytest
from model.biblioteca.biblioteca import Biblioteca, BadRequestException, NotAuthorizedException
from model.biblioteca.libro import Libro
from model.usuarios.usuario import Login
from model.base_datos.administrador_base_datos import Administrador_base_datos
from unittest.mock import MagicMock

@pytest.fixture
def biblioteca():
    return Biblioteca()

@pytest.fixture
def libro_valido():
    return Libro(1, "El Gran Libro", "Autor Ejemplo", 20.5, 10, ["Ficción"], 4.5, "Sinopsis del libro", "/path/del/libro.pdf")

@pytest.fixture
def libro_existente():
    return Libro(1, "Libro Existente", "Autor Existente", 15.0, 5, ["Ficción"], 4.0, "Sinopsis", "/path/del/libro.pdf")

@pytest.fixture
def mock_db():
    mock_db = MagicMock(spec=Administrador_base_datos)
    # Simula la respuesta de read para devolver una lista de usuarios
    mock_db.read.return_value = [
        {"Email": "juan@example.com", "Password": "Contraseña123!", "Nombre": "Juan"}
    ]
    return mock_db

@pytest.fixture
def login_valido():
    return Login("Juan", "juan@example.com", "Contraseña123!")

# Tests de Biblioteca

def test_agregar_libro_duplicado(biblioteca, libro_existente, libro_valido):
    biblioteca.agregar_libro(libro_existente)
    with pytest.raises(BadRequestException, match="El libro con ID 1 ya existe."):
        biblioteca.agregar_libro(libro_valido)

def test_agregar_libro_incompleto(biblioteca):
    libro_incompleto = Libro(2, "", "", 10.0, 0, ["Drama"], 3.0, "Sinopsis", "/path/del/libro.pdf")
    with pytest.raises(BadRequestException, match="El libro debe tener un título y un autor."):
        biblioteca.agregar_libro(libro_incompleto)

# Tests de Login

def test_iniciar_sesion_incorrecto(mock_db, login_valido):
    # Simulamos que las credenciales son incorrectas
    login_valido.db = mock_db  # Inyectamos el mock de db en el objeto Login
    login_valido.email = "incorrecto@example.com"
    login_valido.password = "ContraseñaErronea"
    
    with pytest.raises(NotAuthorizedException, match="Email o contraseña incorrectos."):
        login_valido.iniciarSesion()
