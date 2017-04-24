__author__ = 'crist'

import WBSV_AYD1
from flask. import


class BD():

    __mysql = None

    def __init__(self):
        WBSV_AYD1.config['MYSQL_DATABASE_USER'] = 'root'
        WBSV_AYD1.app.config['MYSQL_DATABASE_PASSWORD'] = 'ayd2017'
        WBSV_AYD1.app.config['MYSQL_DATABASE_DB'] = 'proyectoClase'
        WBSV_AYD1.app.config['MYSQL_DATABASE_HOST'] = 'localhost'
        self.__mysql = MySQL()
        self.__mysql.init_app(WBSV_AYD1.app)

    def get_mysql(self):
        return self.__mysql
