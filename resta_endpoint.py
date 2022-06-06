from flask import Flask
from flask import request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/restar', methods = ['POST'])
def init():
    number1 = request.json["number1"]
    number2 = request.json["number2"]
    return {
        "resultado": number1 - number2
    }
@app.route("/", methods=["GET"])
def initServer():
    return {
        "message": "Servidor iniciado"
    }

if (__name__ == '__main__'):
    app.run(host='localhost', port = 3000, debug = True)