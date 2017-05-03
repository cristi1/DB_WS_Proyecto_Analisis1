__author__ = 'cristi'


# API de PyUnit para pruebas unitarias
import Professor
import Class

import unittest


class WBSVTTest(unittest.TestCase):

    def setUp(self):
        self.professor = Professor.Professor('Felix10', '87632', 'Garcia Felix', 'felix@gmail.com')


    def test_login_professor(self):
        self.assertEqual("{\"mensaje\": \"usuario existente\"}", self.professor.login_professor())

    def test_search_professor(self):
        professor_user = 'Felix10'
        self.assertEquals(True, self.professor.search_professor(professor_user))

    def test_insert_professor(self):
        professor_name = 'Auxiliar3'
        professor_user = 'AuxiliarPrueba3'
        professor_pass = '905670'
        professor_email = 'auxiliatura@gmail.com'
        professor_insert = Professor.Professor(professor_name,professor_user,professor_pass, professor_email)
        self.assertEquals("{\"mensaje\": \"usuario creado con exito\"}", professor_insert.insert_professor())

    if __name__ == "__main__":
        unittest.main()