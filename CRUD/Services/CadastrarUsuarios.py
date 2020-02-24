from Models.Usuarios import usuarios 
from flask import request

def CadastrarUsuario():
    dados = request.get_json()
    
    usuario = {}
    usuario["id"] = dados["id"]
    usuario["nome"] = dados["nome"]
    usuario["email"] = dados["email"]
    usuario["telefone"] = dados["telefone"]
    usuarios.append(usuario)

    return usuarios