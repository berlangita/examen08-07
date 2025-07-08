from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/holamundo')
def holamundo():
    mensaje = {'mensaje': 'Hola Mundo desde Flask!'}
    return jsonify(mensaje)