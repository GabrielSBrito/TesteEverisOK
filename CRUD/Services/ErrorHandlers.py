from Models.Response import response
from flask import jsonify
from Server import app

@app.errorhandler(404)
def TratarErroNotFound(error):
    response["Status"] = "Erro"
    response["Dados"] = "" 
    response["Mensagem"] = "Ação solicitada não disponível"
    return jsonify(response)

@app.errorhandler(500)
def TratarErroNotInterno(error):
    response["Status"] = "Erro"
    response["Dados"] = "{0}".format(error)
    response["Mensagem"] = "Desculpe temos um problema"
    return jsonify(response)

@app.errorhandler(403)
def TratarErroNotInterno(error):
    response["Status"] = "Erro"
    response["Dados"] = "{0}".format(error)
    response["Mensagem"] = "Acesso não permitido"
    return jsonify(response)

@app.errorhandler(400)
def TratarErroNotInterno(error):
    response["Status"] = "Erro"
    response["Dados"] = "{0}".format(error)
    response["Mensagem"] = "Páginão solicitada invalida"
    return jsonify(response)




