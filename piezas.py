class Pieza:
    def __init__(self, tablero):
        self.tablero = tablero
    
    def mover(self, origen, destino):
        get = self.tablero.GET(origen)
        self.tablero.MD(origen, "")
        self.tablero.MD(destino, get)
    
    def colision_detector(self, destino):
        if self.tablero.GET(destino, True) is not True:
            return True
        return False