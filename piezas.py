class Pieza:
    """
    Clase que encarga de manejar las piezas y las funciones asociadas a ellas.
    """
    def __init__(self, tablero):
        self.tablero = tablero

    def mover(self, origen: tuple, destino: tuple):
        """Funcion que se encarga de mover la pieza.

        esta funcion evalua todas las condiciones para que una pieza logre moverse las cuales son:

        -que no exista pieza en el destino
        -que cumpla el movimiento permitido de cada pieza (peon, caballo, ect)
        -que no hallan piezas estorbando
        """
        self.origen = origen
        self.destino = destino
        bypas = self.movimiento_permitido()

        get = self.tablero.GET(self.origen)
        if self._colision_detector(self.destino) and bypas:
            # Evalua si existe una pieza en el destino
            self.tablero.MD(self.origen, "")
            self.tablero.MD(self.destino, get)
            return True
        if bypas is False:
            # Evalua si el movimiento es permitido
            print("Infrige el movimiento permitido de la pieza")
            return False
        print("Ya existe una pieza en el destino")
        return False

    def movimiento_permitido(self):
        return True

    def _colision_detector(self, destino):
        """condicional que te detecta si hay piezas en el destino y si hay piezas estorbando."""

        if not self.tablero.GET(self.destino, True):
            return True
        return False


class Peon(Pieza):

    def movimiento_permitido(self):
        if self.origen[1] - 1 == self.destino[1] and self.origen[2] == self.destino[2]:
            return True
        elif (self.origen[1] - 1 == self.destino) is not True:
            print("row no permitida para el tipo de pieza")
        elif (self.origen[2] == self.destino) is not True:
            print("columna no permitida para la pieza")
        return False