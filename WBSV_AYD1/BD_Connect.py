__author__ = 'crist'

import WBSV_AYD1
from flask.ext.mysql import MySQL


class BD():

    def __init__(self):
        self.__mysql = MySQL()
        WBSV_AYD1.app.config['MYSQL_DATABASE_USER'] = 'root'
        WBSV_AYD1.app.config['MYSQL_DATABASE_PASSWORD'] = 'ayd2017'
        WBSV_AYD1.app.config['MYSQL_DATABASE_DB'] = 'proyectoClase'
        WBSV_AYD1.app.config['MYSQL_DATABASE_HOST'] = 'localhost'
        self.__mysql.init_app(WBSV_AYD1.app)

    def get_mysql(self):
        return self.__mysql
