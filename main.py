from piezas import Pieza
from tablero import Tablero
class Ajedres:
    def __init__(self):
        self.tablero = Tablero()
        self.piezas = Pieza(self.tablero)
    
    def turno(self):
        while True:
            origen = input("que pieza desea mover?\n")
            plz = input("hacia donde desea moverla?")
            if self.piezas.colision_detector(plz):
                self.piezas.mover(origen, plz)
                break
            else:
                print("ya existe una pieza donde quieres pocisionarte")
    def run(self):
        while True:
            self.tablero.display()
            self.turno()

test = Ajedres()
test.run()