class Pieza:
    """
    Clase que encarga de manejar las piezas y las funciones asociadas a ellas.
    """
    def __init__(self, tablero, origen, destino):
        self.tablero = tablero
        self.data = tablero.data
        self.check = True
        self.origen = origen
        self.destino = destino

    def mover(self):
        """Funcion que se encarga de mover la pieza.

        esta funcion modifica la matriz y reeplaza los valores correspndientes
        """
        if self.check:
            get = self.tablero.GET(self.origen)
            self.tablero.MD(self.destino, get)
            self.tablero.MD(self.origen, "")
        print(self.check, "Piezas: 2")
    
    def accion(self):
        self.movimiento_permitido()
        self._colision_detector()
        self.mover()
        return self.check 

    def movimiento_permitido(self):
        return True

    def _colision_detector(self):
        """condicional que te detecta si hay piezas en el destino y si hay piezas estorbando."""
        if self.tablero.GET(self.destino):
            self.check = False
            print("Ya existe una pieza en el destino")
        print(self.check, "Piezas: 1")


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

        direccion = self.tablero.GET(self.origen)
        valor = help_(direccion[0])
        movimiento_(valor)        
        print(self.check, "Piezas: 0")


class Torre(Pieza):
    def movimiento_permitido(self):
        pass

    def _colision_detector(self):
        pass


class Alfil(Pieza):
    pass
