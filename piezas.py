class Pieza:
    """
    Clase que encarga de manejar las piezas y las funciones asociadas a ellas.
    """
    def __init__(self, tablero, origen, destino, ta):
        self.tablero = tablero
        self.data = tablero.data
        self.check = True
        self.origen = origen
        self.destino = destino
        self.ta = ta
        self.get1 = self.tablero.GET(origen)

    def mover(self):
        """Funcion que se encarga de mover la pieza.

        esta funcion modifica la matriz y reeplaza los valores correspndientes
        """
        if self.check:
            self.tablero.MD(self.destino, self.get1)
            self.tablero.MD(self.origen, "")
        print(self.check, "Piezas: 2")
    
    def accion(self):
        self.turno()
        self.movimiento_permitido()
        self._colision_detector()
        self.mover()
        return self.check

    def turno(self):
        if self.get1[0] == self.ta:
            self.check = True
        else:
            print("No puedes mover esta pieza en este turno")
            self.check = False

    def movimiento_permitido(self):
        return True

    def _colision_detector(self):
        return True


class Peon(Pieza):

    def movimiento_permitido(self):

        def help_(Turno):
            if Turno == "W":
                valor = -1
            elif Turno == "B":
                valor = 1
            return valor

        def movimiento_(valor):
            row1, column1 = self.origen[1:]

            row2, column2 = self.destino[1:]
            check = 0
            if (row1 + valor) != row2:
                print("row no permitida para el tipo de pieza")
                check += 1
            if column1 != column2:
                print("columna no permitida para la pieza")
                check += 1
            if check > 0:
                self.check = False

        valor = help_(self.get1[0])
        movimiento_(valor)        
        print(self.check, "Piezas: 0")


class Torre(Pieza):
    def movimiento_permitido(self):
        pass

    def _colision_detector(self):
        pass


class Alfil(Pieza):
    pass
