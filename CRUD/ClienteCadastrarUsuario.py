import requests as req 

url = "http://localhost:8080/usuarios"

d = {
    "Usuarios" : [
            {"id": "1", "nome":"Gabriel Brito", "email": "GabrielBrito@gmail.com", "telefone": "1111-1111"},
            {"id": "2", "nome":"Rafael Alves", "email": "RafaelAlves@gmail.com", "telefone": "2222-2222"},
            {"id": "3", "nome":"Monique Moreno", "email": "MoniqueMoreno@gmail.com", "telefone": "3333-3333"},
            {"id": "4", "nome":"Jose Luis", "email": "JoseLuis@gmail.com", "telefone": "4444-4444"},
            {"id": "5", "nome":"Diego Augusto", "email": "DiegoAugusto@gmail.com", "telefone": "5555-5555"},
    ]
}

retorno = d["Usuarios"]


for dados in retorno:
    retorno = req.api.post(url, json=dados).json()
    print("Usuario: ",dados['nome'], " Adicionado !!!")


    