import unittest
from figuras import Figuras

class TestFiguras(unittest.TestCase):

	def setUp(self):
		self.figura = Figuras()


	def test_area_cuadrado_lado_5(self):
		resultado = self.figura.cuadrado(5)
		self.assertEquals(25,resultado)

	def test_area_cuadrado_lado_6(self):
		resultado = self.figura.cuadrado(6)
		self.assertEquals(36,resultado)

	def test_area_cuadrado_lado_g(self):
		resultado = self.figura.cuadrado('g')
		self.assertEquals('dato incorrecto',resultado)

	def test_area_cuadrado_lado_4(self):
		resultado = self.figura.cuadrado(4.5)
		self.assertEquals(16,resultado)

	def test_area_rectangulo_base_2_altura_3(self):
		resultado = self.figura.rectangulo(2,3)
		self.assertEquals(6,resultado)

	def test_area_rectangulo_base__2_altura_3(self):
		resultado = self.figura.rectangulo(-2,3)
		self.assertEquals(-6,resultado)

	def test_area_rectangulo_base__2_altura__3(self):
		resultado = self.figura.rectangulo(-2,-3)
		self.assertEquals(6,resultado)

	def test_area_rectangulo_base_2_altura_g(self):
		resultado = self.figura.rectangulo(2,'g')
		self.assertEquals('dato incorrecto',resultado)

	def test_area_rectangulo_base_g_altura_2(self):
		resultado = self.figura.rectangulo('g',2)
		self.assertEquals('dato incorrecto',resultado)

	def test_area_rectangulo_base_g_altura_f(self):
		resultado = self.figura.rectangulo('g','f')
		self.assertEquals('dato incorrecto',resultado)

	def test_area_triangulo_base_5_altura_2(self):
		resultado = self.figura.triangulo(5,2)
		self.assertEquals(5,resultado)

	def test_area_triangulo_base__5_altura_2(self):
		resultado = self.figura.triangulo(-5,2)
		self.assertEquals(-5,resultado)

	def test_area_triangulo_base_e_altura_2(self):
		resultado = self.figura.triangulo('e',2)
		self.assertEquals('dato incorrecto',resultado)

	def test_area_triangulo_base_3_altura_f(self):
		resultado = self.figura.triangulo(3,'f')
		self.assertEquals('dato incorrecto',resultado)

	def test_area_triangulo_base_c_altura_f(self):
		resultado = self.figura.triangulo('c','f')
		self.assertEquals('dato incorrecto',resultado)

	def test_area_circulo_radio_3(self):
		resultado = self.figura.circulo(3)
		self.assertEquals(28.2744 ,resultado)

	def test_area_circulo_radio_g(self):
		resultado = self.figura.circulo('g')
		self.assertEquals('dato incorrecto' ,resultado)

	def test_area_circulo_radio__3(self):
		resultado = self.figura.circulo(-3)
		self.assertEquals(28.2744 ,resultado)




#rectangulo, triangulo, circulo



	def tearDown(self):
		pass

if __name__ == '__main__':
	unittest.main()
