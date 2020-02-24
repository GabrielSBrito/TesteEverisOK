from flask import Flask
from flask import jsonify

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False   #Config para Não bugar acentos

from Services.Routes import *
from Services.ErrorHandlers import *

if __name__ == "__main__":
    app.run(port=8080, debug=True)
    
