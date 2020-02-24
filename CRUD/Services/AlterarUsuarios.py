from Models.Usuarios import usuarios 
from flask import request

from flask import jsonify
from Models.Response import response
from Server import app

def AlterarUsuarios(id):
    usuarioss = {}
    dados = request.get_json()
    for x in usuarios:
        if x["id"] == id:
            x["id"] = dados["id"]
            x["nome"] = dados["nome"]
            x["email"] = dados["email"]
            x["telefone"] = dados["telefone"]
    return usuarioss