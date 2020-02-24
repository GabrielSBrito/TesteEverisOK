import requests as req 
                                            
url = "http://localhost:8080/usuarios/delete/{0}". format("5")  # format("4") = Usuario que deseja deletar


retorno = req.api.delete(url).json()

print(retorno)

