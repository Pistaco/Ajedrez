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
        get = self.tablero.GET(origen)
        if self._colision_detector(destino) and self.movimiento_permitido():
            # Evalua si existe una pieza en el destino
            self.tablero.MD(origen, "")
            self.tablero.MD(destino, get)
            return True
        if self.movimiento_permitido() is False:
            # Evalua si el movimiento es permitido
            print("Infrige el movimiento permitido de la pieza")
            return False
        print("Ya existe una pieza en el destino")
        return False

    def movimiento_permitido(self):
        return True

    def _colision_detector(self, destino):
        """condicional que te detecta si hay piezas en el destino y si hay piezas estorbando."""

        if not self.tablero.GET(destino, True):
            return True
        return False
