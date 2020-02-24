from Models.Usuarios import usuarios
from flask import request

def DeletarUsuario(id):
    for x in usuarios:
        if x["id"] == id:
            usuarios.remove(x)
            return usuarios
    return None
