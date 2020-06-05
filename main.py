from piezas import Pieza
from tablero import Tablero
class Ajedres:
    def __init__(self):
        self.tablero = Tablero()
        self.piezas = Pieza(self.tablero)
        self.turnoactual = "W"
    
    def __switchturn(self):
        if self.turnoactual == "W":
            self.turnoactual = "B"
        if self.turnoactual == "B":
            self.turnoactual = "W"
    
    def _info_(self):
        while True:
            input_ = input("que pieza desea mover?\n")
            if input_[1].upper() not in tuple("ABCDEFGH"):
                print("ingresaste un valor incorrecto")
            elif int(input_[2]) not in tuple(range(1, 8)):
                print("ingresaste un valor incorrecto")
            else:
                return input_

    def turno(self):
        while True:
            coo = self._info_
            plz = self._info_
            if self.piezas.colision_detector:
                self.piezas.mover(coo, plz)
                break
            else:
                print("ya hay una pieza aqui")


    def run(self):
        while True:
            self.tablero.display()
            self.turno()

test = Ajedres()
test.run()