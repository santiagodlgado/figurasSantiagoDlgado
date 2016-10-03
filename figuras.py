from math import pi


class Figuras:

    def cuadrado(self, lado):

        try:
            lado = int(lado)
            return lado * lado
        except Exception, e:
            return 'dato incorrecto'

    def rectangulo(self, b, h):
        try:
            b = int(b)
            h = int(h)
            return (b * h)
        except Exception, e:
            return 'dato incorrecto'

    def triangulo(self, b, h):
        try:
            b = int(b)
            h = int(h)
            return (b * h) / 2
        except Exception, e:
            return 'dato incorrecto'

    def circulo(self, radio):
        try:
            radio = int(radio)
            pi = 3.1416

            radioC = radio * radio
            #result= math.pi*radioC
            result = pi * radioC
            return result
        except Exception, e:
            return 'dato incorrecto'
