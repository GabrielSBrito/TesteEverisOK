from flask import jsonify
from Models.Response import response
from Server import app

from Services.ListarUsuarios import ListarUsuarios
from Services.CadastrarUsuarios import CadastrarUsuario
from Services.ConsultarPorID import ConsultarPorID
from Services.AlterarUsuarios import AlterarUsuarios
from Services.DeletarUsuario import DeletarUsuario


@app.route("/usuarios", methods=["GET"])
def ListarUsuariosRota():
    response["Status"] = "Sucesso"
    response["Dados"] = ListarUsuarios()
    response["Mensagem"] = "Lista de Usuarios"
    return jsonify(response)

@app.route("/usuarios",methods=["POST"])    
def CadastrarUsuarioRota():
    response["Status"] = "Sucesso"
    response["Dados"] = CadastrarUsuario()
    response["Mensagem"] = "Usuario Cadastrado!!!!"
    return jsonify(response)

@app.route("/usuarios/<id>", methods=["GET"])
def ConsultarPorRARota(id):
    response["Status"] = "Sucesso"
    response["Mensagem"] = "Usuario Encontrado!"
    response["Dados"] = ConsultarPorID(id)
    return jsonify(response)

@app.route("/usuarios/add/<id>",methods=["PUT"])
def AlterarUsuarioRota(id):
    response["Status"] = "Sucesso"
    response["Dados"] = AlterarUsuarios(id)
    response["Mensagem"] = "Dados do Usuario alterados!!!!"
    return jsonify(response)

@app.route("/usuarios/delete/<id>",methods=["GET","DELETE"])
def DeletarUsuarioRota(id):
    if DeletarUsuario(id) == None:
        response["Status"] = "Sucesso"
        response["Mensagem"] = "Usuario de ID={0} Não Encontrado para ser Deletado".format(id)
        #response["Dados"] = []
        return jsonify(response)
    else:
        response["Status"] = "Sucesso"
        response["Mensagem"] = "Usuario de ID= {0} Deletado!!!!!".format(id)
        response["Dados"] = DeletarUsuario(id)
        return jsonify(response)
    

    



