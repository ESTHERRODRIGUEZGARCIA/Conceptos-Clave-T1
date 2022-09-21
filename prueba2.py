import math
class Punto():

    x = 0
    y = 0

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

    def distancia():
        print("La distancia es:", math.sqrt((p1.x-p2.x)**2 + (p1.y-p2.y)**2))

    def rectangulo(punto):


A = (2,3)
B = (5,5)
C = (-3,-1)
D = (0,0)





