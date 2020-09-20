from flask import Flask

app = Flask(__name__)

@app.route('/init')
def myFistFuncion():
    return 'Estou aqui'