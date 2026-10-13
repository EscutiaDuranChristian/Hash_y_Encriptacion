# Importa todas las funciones desde el archivo handlers.py
from .handlers import root, login, logout, UsersView, form_user, create_user, Delete, UpdatePage, Update, verUsuario

# Definir qué funciones estarán disponibles al importar controllers
__all__ = ['root', 'login', 'logout', 'UsersView', 'form_user', 'create_user', 'Delete', 'UpdatePage', 'Update', 'verUsuario']
