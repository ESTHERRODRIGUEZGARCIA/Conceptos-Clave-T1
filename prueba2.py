import math
import random

A = (2,3)
B = (5,5)
C = (-3,-1)
D = (0,0)
class Punto():

    x = 0
    y = 0
    p1 = random.choice(A, B, C, D)
    p2 = random.choice(A, B, C, D)

    def __innit__(self, x, y):
        #método constructor
        self.x = x
        self.y = y

    def __str__(self):
        return "(X={},Y={})".format(self.x, self.y)

    def cuadrante(self, x, y):
        #me debe indicar a qué cuadrante pertenece el punto
        if x > 0 and y > 0:
            print("El punto se encuentra en el cuadrante 1")
        if x < 0 and y > 0:
            print("El punto se encuentra en el cuadrante 2")
        if x > 0 and y < 0:
            print("El punto se encuentra en el cuadrante 3")
        if x < 0 and y < 0:
            print("El punto se encuentra en el cuadrante 4")
        elif x == 0 and y == 0:
            print("El punto se encuentra sobre el origen")

    def vector(self, vector, x, y):
        vector = x - y
        print("El vector entre {} y {} es: ({}, {}) ", vector)

    def distancia(punto, p1, p2):
        print("La distancia es:", math.sqrt((p1.x-p2.x)**2 + (p1.y-p2.y)**2))

class Rectangulo():

    def __innit__(self, punto_inicial, punto_final):
        #método constructor
        self.punto_inicial = punto_inicial
        self.punto_final = punto_final
    
    def base(self):
        Base = self.vBase
        print("La base del rectángulo es {}".format(Base ))
 
    def altura(self):
        Altura = self.vAltura
        print("La altura del rectángulo es {}".format(Altura))
 
    def area(self):
        Area = self.vArea
        print("El área del rectángulo es {}".format(Area))













