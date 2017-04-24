__author__ = 'crist'

import BD_Connect

import json

class Professor:

    __professor_user = None
    __professor_password = None
    __professor_name = None
    __professor_email = None

    def __init__(self,pu,ps,pn,pe):
        self.__professor_user = pu
        self.__professor_password = ps
        self.__professor_name = pn
        self.__professor_email = pe


    def insert_professor(self):
        professor_result = self.search_professor(self.__professor_user) #Verificar si el usuario ya existia
        conn = None
        cursor = None
        if professor_result == False: #Si no existe continuar con el procedimiento
            try:
                if self.__professor_name != "" and self.__professor_user != "" and self.__professor_password != "" :
                    print("si entro a ejecutar codigo")
                    mysql_aux = BD_Connect.BD()
                    mysql = mysql_aux.get_mysql()
                    conn = mysql.connect()
                    cursor = conn.cursor()
                    cursor.callproc('sp_insertarUsuario',(self.__professor_name, self.__professor_user, self.__professor_password, self.__professor_email))
                    data = cursor.fetchall()
                    if len(data) is 0:
                        conn.commit()
                        return json.dumps({'mensaje' : 'usuario creado con exito'})
                    else:
                        professor_result = {'mensaje' : 'Error en la creacion del usuario'}
                        return json.dumps(professor_result)
                else:
                    professor_result = {'mensaje' : 'Error en la creacion del usuario'}
                    return json.dumps(professor_result)
            except Exception as e:
                    professor_result = {'mensaje' : str(e)}
                    return json.dumps(professor_result)
            finally:
                cursor.close()
                conn.close()
        else:
            professor_result = {'mensaje' : 'Error, El usuario ya existe'}
            return json.dumps(professor_result)


    def search_professor(self,pu):
        professor_user = pu
        professor_result = None
        conn = None
        cursor = None
        try:
            if professor_user != "":
                mysql_aux = BD_Connect.BD()
                mysql = mysql_aux.get_mysql()
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

    def login_professor(self):
        professor_result = None
        conn = None
        cursor = None
        try:
            if self.__professor_user != "" and self.__professor_password != "" :
                mysql_aux = BD_Connect.BD()
                mysql = mysql_aux.get_mysql()
                conn = mysql.connect()
                cursor = conn.cursor()
                cursor.callproc('sp_login',(self.__professor_user,self.__professor_password))
                data = cursor.fetchall()
                if len(data) is 1:
                    conn.commit()
                    return json.dumps({'mensaje' : 'usuario existente'})
                else:
                    professor_result = {'mensaje' : 'Error, no se encontro el usuario'}
                    return json.dumps(professor_result)
            else:
                professor_result = {'mensaje' : 'Error, no hay informacion de referencia'}
                return json.dumps(professor_result)
        except Exception as e:
            print('mi error: ' + str(e))
            professor_result = {'mensaje' : str(e)}
            return json.dumps(professor_result)
        finally:
            cursor.close()
            conn.close()