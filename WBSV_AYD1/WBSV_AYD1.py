#python tiene una API de PyUnit para pruebas unitarias
import unittest
import json
import WBSVTest
import requests
import status


from flask import Flask, request, render_template
from flask.ext.api import FlaskAPI, status, exceptions
from flask.ext.mysql import MySQL

mysql = MySQL()

app = Flask(__name__)
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'ayd2017'
app.config['MYSQL_DATABASE_DB'] = 'proyectoClase'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

mysql.init_app(app)

@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/user_professor/new', methods=['POST', 'PATCH', 'DELETE', 'GET'])
def professor_new():
    if request.method == 'POST': #creamos el usuario profesor
        json_professor = request.json
        json_result = json_professor
        professor_name = json_professor['nombre']
        professor_user = json_professor['usuario']
        professor_pass = json_professor['contrasenia']
        insert_professor(professor_name,professor_user,professor_pass)
    elif request.method == 'PATH': #actualizar info profesor
        json_professor = request.json
        json_result = json_professor
        return json.dump({'mensaje' : 'usuario actualizado con exito'}), status.HTTP_200_OK
    elif request.method == 'DELETE': #Eliminar profesor
        json_professor = request.json
        json_result = json_professor
        return json.dump({'mensaje' : 'usuario eliminado con exito'}), status.HTTP_200_OK
    else: # mostrar informacion de profesor
        json_result = {'mensaje' : 'en construccion'}
        return json.dumps(json_result), status.HTTP_201_CREATED

@app.route('/user_professor/list', methods=['POST', 'GET'])
def professor_log():
    if request.method == 'POST': #login
        json_professor = request.json
        json_result = json_professor
        professor_user = json_professor['usuario']
        professor_pass = json_professor['contrasenia']
        return login_professor(professor_user,professor_pass)
    else:
        json_result = {'mensaje' : 'en constuccion'}, status.HTTP_202_ACCEPTED
        return json.dumps(json_result)

@app.route('/user_professor/exist', methods=['POST', 'GET'])
def professor_search():
    if request.method == 'POST': #verificacion que el usuario exista
        json_professor = request.json
        json_result = json_professor
        professor_user = json_professor['usuario']
        professor_pass = json_professor['contrasenia']
        search_professor(professor_user)
    else:
        json_result = {'mensaje' : 'en constuccion'}, status.HTTP_202_ACCEPTED
        return json.dumps(json_result)

@app.route('/test_professor', methods=['GET'])
def test_professor():
    return render_template('Test_Professor.html')

#############################METODOS###################################
def insert_professor(pn,pu,ps):
    professor_name = pn
    professor_user = pu
    professor_pass = ps
    professor_result = search_professor(pu) #Verificar si el usuario ya existia
    if professor_result == False: #Si no existe continuar con el procedimiento
        try:
            if professor_name != "" and professor_user != "" and professor_pass != "" :
                conn = mysql.connect()
                cursor = conn.cursor()
                cursor.callproc('sp_insertarUsuario',(professor_name,professor_user,professor_pass))
                data = cursor.fetchall()
                if len(data) is 0:
                    conn.commit()
                    return json.dumps({'mensaje' : 'usuario creado con exito'})#, status.HTTP_201_CREATED
                else:
                    professor_result = {'mensaje' : 'Error en la creacion del usuario'}
                    return json.dumps(professor_result), status.HTTP_400_BAD_REQUEST
            else:
                professor_result = {'mensaje' : 'Error en la creacion del usuario'}
                return json.dumps(professor_result), status.HTTP_400_BAD_REQUEST
        except Exception as e:
                professor_result = {'mensaje' : str(e)}
                return json.dumps(professor_result), status.HTTP_400_BAD_REQUEST
        finally:
            cursor.close()
            conn.close()
    else:
        professor_result = {'mensaje' : 'Error, El usuario ya existe'}
        return json.dumps(professor_result), status.HTTP_400_BAD_REQUEST

def search_professor(pu):
    professor_user = pu
    professor_result = None
    try:
        if professor_user != "":
            conn = mysql.connect()
            cursor = conn.cursor()
            #cursor.callproc('sp_existUsuario', (professor_user))
            cursor.execute("CALL sp_ExistUsuario('"+  professor_user+ "')")
            data = cursor.fetchone()
            #data = cursor.fetchall()
            if len(data) is 1:
                conn.commit()
                return True
            else:
                professor_result = {'mensaje' : 'Error, no se encontro el usuario'}
                return False
        else:
            professor_result = {'mensaje' : 'Error, no hay informacion de referencia'}
            return False
    except Exception as e:
            professor_result = {'mensaje' : str(e)}
            return False
    finally:
        cursor.close()
        conn.close()

def login_professor(pu, ps):
    professor_user = pu
    professor_pass = ps
    professor_result = None
    try:
        if professor_user != "" and professor_pass != "" :
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.callproc('sp_login',(professor_user,professor_pass))
            data = cursor.fetchall()
            if len(data) is 1:
                conn.commit()
                return json.dumps({'mensaje' : 'usuario existente'})#, status.HTTP_200_CREATED
            else:
                professor_result = {'mensaje' : 'Error, no se encontro el usuario'}
                return json.dumps(professor_result)#, status.HTTP_400_BAD_REQUEST
        else:
            professor_result = {'mensaje' : 'Error, no hay informacion de referencia'}
            return json.dumps(professor_result)#, status.HTTP_400_BAD_REQUEST
    except Exception as e:
            print('mi error: ' + str(e))
            professor_result = {'mensaje' : str(e)}
            return json.dumps(professor_result)#, status.HTTP_400_BAD_REQUEST
    finally:
        cursor.close()
        conn.close()


class WBSVTTest(unittest.TestCase):

    def test_login_professor(self):
        professor_user = 'Felix10'
        professor_pass = '87632'
        self.assertEqual("{\"mensaje\": \"usuario existente\"}", login_professor(professor_user, professor_pass))

    def test_search_professor(self):
        professor_user = 'Felix10'
        self.assertEquals(True, search_professor(professor_user))

    def test_insert_professor(self):
        professor_name = 'Auxiliar3'
        professor_user = 'AuxiliarPrueba3'
        professor_pass = '905670'
        self.assertEquals("{\"mensaje\": \"usuario creado con exito\"}", insert_professor(professor_name,professor_user,professor_pass))


if __name__ == '__main__':
    #unittest.main()
    app.run(host='192.168.1.16', debug=True)
