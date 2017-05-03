__author__ = 'crist'

import unittest
import Class

class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.clase = Class.Class('Redes 2', 5)

    def test_insert_class(self):
        self.clase_insertar = Class.Class('Vacaciones2017',1);
        self.assertEqual("{\"mensaje\": \"curso creado con exito\"}", self.clase_insertar.insert_class())

    def test_search_curso(self):
        class_name = 'Redes 2'
        self.assertEquals(True, self.clase.search_class(class_name))

if __name__ == '__main__':
    unittest.main()
