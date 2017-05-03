__author__ = 'cristian'

import BD_Connect
import json

class Class:
    __class_name = None
    __class_cod_professor = None

    def __init__(self, cn, cp):
        self.__class_name = cn
        self.__class_cod_professor = cp
        self.__class_cod_class = ''

    def insert_class(self):
        class_result = self.search_class(self.__class_name)  # Verificar si el usuario ya existia
        conn = None
        cursor = None
        if class_result == False:  # Si no existe continuar con el procedimiento
            try:
                if self.__class_name != "" and self.__class_cod_professor != "" :
                    mysql_aux = BD_Connect.BD()
                    mysql = mysql_aux.get_mysql()
                    conn = mysql.connect()
                    cursor = conn.cursor()
                    cursor.callproc('sp_insertarCurso', (self.__class_name, self.__class_cod_professor, self.__class_cod_class))
                    data = cursor.fetchall()
                    if len(data) is 0:
                        conn.commit()
                        return json.dumps({'mensaje': 'curso creado con exito'})
                    else:
                        class_result = {'mensaje': 'Error en la creacion del curso'}
                        return json.dumps(class_result)
                else:
                    class_result = {'mensaje': 'Error en la creacion del curso'}
                    return json.dumps(class_result)
            except Exception as e:
                class_result = {'mensaje': str(e)}
                return json.dumps(class_result)
            finally:
                cursor.close()
                conn.close()
        else:
            class_result = {'mensaje': 'Error, El curso ya existe'}
            return json.dumps(class_result)

    def search_class(self, cn):
        class_name =  cn
        class_result = None
        conn = None
        cursor = None
        try:
            if class_name != "":
                mysql_aux = BD_Connect.BD()
                mysql = mysql_aux.get_mysql()
                conn = mysql.connect()
                cursor = conn.cursor()
                # cursor.callproc('sp_existCurso', (class_name))
                cursor.execute("CALL sp_ExistCurso('" + class_name + "')")
                data = cursor.fetchone()
                #data = cursor.fetchall()
                if len(data) is 1:
                    conn.commit()
                    return True
                else:
                    class_result = {'mensaje': 'Error, no se encontro el curso'}
                    return False
            else:
                class_result = {'mensaje': 'Error, no hay informacion de referencia'}
                return False
        except Exception as e:
            class_result = {'mensaje': str(e)}
            return False
        finally:
            cursor.close()
            conn.close()

