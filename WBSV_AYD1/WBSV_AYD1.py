__author__ = 'cristian'

import Professor
import WBSVTest

import unittest
import json

from flask import Flask, request, render_template
from flask.ext.api import status

app = Flask(__name__)


@app.route('/')
def hello_world():
    # return 'Hello World!'
    professor_object = Professor.Professor('Azurdia90', '1234', 'Azurdia Cristian', 'cristian@gmail.com')
    return professor_object.list_professor_class(5)

@app.route('/user_professor/new', methods=['POST', 'PATCH', 'DELETE', 'GET'])
def professor_new():
    if request.method == 'POST':  # creamos el usuario profesor
        professor_json = request.json
        json_result = professor_json
        professor_object = Professor.Professor(professor_json['usuario'], professor_json['contrasenia'], professor_json['nombre'],  professor_json['email'])
        return professor_object.insert_professor()
    else: # mostrar informacion de profesor
        json_result = {'mensaje' : 'en construccion'}
        return json.dumps(json_result), status.HTTP_201_CREATED

@app.route('/user_professor/list', methods=['POST', 'GET'])
def professor_log():
    if request.method == 'POST':  # login
        professor_json = request.json
        professor_object = Professor.Professor(professor_json['usuario'], professor_json['contrasenia'], "", "")
        return professor_object.login_professor()
    else:
        json_result = {'mensaje' : 'en constuccion'}, status.HTTP_202_ACCEPTED
        return json.dumps(json_result)

@app.route('/user_professor/exist', methods=['POST', 'GET'])
def professor_search():
    if request.method == 'POST':  # verificacion que el usuario exista
        professor_json = request.json
        professor_object = Professor.Professor("", "", "", "", "")
        return professor_object.search_professor(professor_json['usuario'])
    else:
        json_result = {'mensaje' : 'en constuccion'}, status.HTTP_202_ACCEPTED
        return json.dumps(json_result)

@app.route('/test_professor', methods=['GET'])
def test_professor():
    return render_template('Test_Professor.html')

#############################METODOS###################################


if __name__ == '__main__':
    app.run('172.20.10.4', debug=True)
    #app.run(debug = True)