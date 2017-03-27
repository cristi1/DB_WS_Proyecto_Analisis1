import json
import requests
import status

from flask import Flask, request
from flask.ext.api import FlaskAPI, status, exceptions

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/user_professor', methods=['POST', 'PATCH', 'DELETE', 'GET'])
def professor_methods():
    if request.method == 'POST': #creamos el usuario profesor
        json_professor = request.json
        json_result = json_professor
        professor_user = json_professor['usuario']
        professor_pass = json_professor['contrasenia']
        professor_id = json_professor['identificador']
        professor_name = json_professor['nombre']
        professor_mail = json_professor['correo']
        professor_birthdate = json_professor['fecha_nacimiento']
        return json.dumps({'mensaje' : 'usuario creado con exito'}), status.HTTP_201_CREATED
    elif request.method == 'PATH': #actualizar info profesor
        json_professor = request.json
        json_result = json_professor
        return json.dump({'mensaje' : 'usuario actualizado con exito'}), status.HTTP_200_OK
    elif request.method == 'DELETE': #Eliminar profesor
        json_professor = request.json
        json_result = json_professor
        return json.dump({'mensaje' : 'usuario eliminado con exito'}), status.HTTP_200_OK
    else: # mostrar informacion de profesor
        json_result = {}
        return json_result, status.HTTP_201_CREATED

@app.route('/user_professor/list', methods=['POST', 'GET'])
def log_professor():
    if request.method == 'POST':
        json_professor = request.json
        json_result = json_professor
        professor_user = json_professor['usuario']
        professor_pass = json_professor['contrasenia']

        json_result = {'mensaje' : 'usuario existente'}
        return json.dumps(json_result), status.HTTP_202_ACCEPTED
    else:
        json_result = {'mensaje' : 'usuario existente'}, status.HTTP_202_ACCEPTED
        return json.dumps(json_result)

if __name__ == '__main__':
    app.run()
