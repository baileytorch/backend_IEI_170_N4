from django.test import TestCase
from .models import Nacionalidad,Autor,Comuna

# Create your tests here.
class TestNacionalidad(TestCase):
    def test_objeto_nacionalidad(self):
        nacionalidad = Nacionalidad.objects.create(pais='Chile', nacionalidad='Chileno')

        self.assertEqual(nacionalidad.pais, 'Chile')
        self.assertEqual(nacionalidad.nacionalidad, 'Chileno')
        self.assertTrue(Nacionalidad.objects.filter(pais='Chile').exists())
        
class TestAutor(TestCase):
    def test_objeto_autor(self):
        autor = Autor.objects.create(
            nombre='Ricardo Eliécer Neftalí Reyes Basoalto',
            genero='M')

        self.assertEqual(autor.nombre, 'Ricardo Eliécer Neftalí Reyes Basoalto')
        self.assertEqual(autor.genero, 'M')
        self.assertTrue(Autor.objects.filter(nombre='Ricardo Eliécer Neftalí Reyes Basoalto').exists())
        
class TestComuna(TestCase):
    def test_objeto_autor(self):
        comuna = Comuna.objects.create(
            codigo_comuna='09101',
            nombre_comuna='Temuco')

        self.assertEqual(comuna.codigo_comuna, '09101')
        self.assertNotEqual(comuna.codigo_comuna, '09110')
        self.assertEqual(comuna.nombre_comuna, 'Temuco')
        self.assertTrue(Comuna.objects.filter(codigo_comuna='09101').exists())
        self.assertFalse(Comuna.objects.filter(codigo_comuna='00000').exists())