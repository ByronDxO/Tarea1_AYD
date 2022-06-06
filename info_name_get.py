from flask import Flask

from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/', methods = ['GET'])
def init():
    return {
        "Identificacion": "Byron Rubén Hernández de León - 201806840"
    }

# STARTING THE SERVER
if (__name__ == '__main__'):
    app.run(host='localhost', port = 4000, debug = True)