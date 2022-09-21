class Punto():

    x = 0
    y = 0

    def __innit__(self, x, y):
        #método constructor
        self.x = x
        self.y = y

    def __str__(self):
        return "(X={},Y={})".format(self.x, self.y)

    def cuadrante():
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



