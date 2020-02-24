import requests as req 
#                                       ra do aluno que deseja alterar
url = "http://localhost:8080/usuarios/add/{0}".format("1")
dados = {"id": "9999999", "nome" : "ZZZZZZZZZZZZZZZZZZ", "email" : "yyyyyyyyyyyyyyy@gmail.com", "telefone": "9999-9999"}

retorno = req.api.put(url, json=dados).json()

print(retorno)