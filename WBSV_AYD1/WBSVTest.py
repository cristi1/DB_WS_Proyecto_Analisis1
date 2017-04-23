#API de PyUnit para pruebas unitarias

import WBSV_AYD1
import Professor

import unittest

class WBSVTTest(unittest.TestCase):

    Professor.Professor('Felix10','87632','Felix Garcia','')


    def test_login_professor(self):
        professor_user = 'Felix10'
        professor_pass =  '87632'
        self.assertEqual("{\"mensaje\": \"usuario existente\"}", WBSV_AYD1.login_professor(professor_user, professor_pass))

    def test_search_professor(self):
        professor_user = 'Felix10'
        self.assertEquals(True, WBSV_AYD1.search_professor(professor_user))

    def test_insert_professor(self):
        professor_name = 'Auxiliar3'
        professor_user = 'AuxiliarPrueba3'
        professor_pass = '905670'
        professor_email = 'auxiliatura@gmail.com'
        self.assertEquals("{\"mensaje\": \"usuario creado con exito\"}", WBSV_AYD1.insert_professor(professor_name,professor_user,professor_pass,professor_email))



