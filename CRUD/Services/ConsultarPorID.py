from Models.Usuarios import usuarios
from Models.Response import response

usuario = {}
def ConsultarPorID(id):
    
    for x in usuarios:
        if x["id"] == id:
            response["Mensagem"] = "Usuario Encontrado!"
            usuario = x 
            break
        else:
            response["Mensagem"] = "Usuario NÃO Encontrado!!!!!"
            usuario = {}
    return usuario
