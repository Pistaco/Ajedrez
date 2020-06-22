from piezas import Pieza, Peon, Torre, Alfil, Caballo, Reina, Rey
from tablero import Tablero
from check import Check

class Ajedres:
    def __init__(self):
        self.tablero = Tablero()
        self.turnoactual = "W"
        self.check = Check(self)
        self.texto = {"W": "Las blancas!", "B": "Las negras!"}
        self.victoria = False

    def __switchturn(self):
        if self.turnoactual == "W":
            self.turnoactual = "B"
        elif self.turnoactual == "B":
            self.turnoactual = "W"

    def turno(self):
        while True:
            self.coo, self.plz = self.check.run()
            self.seleccionador_()
            if self.pactual(self).accion():
                break

    def checklose(self):
        matriz = self.tablero.data == "WK"
        matriz2 = self.tablero.data == "BK"
        if matriz.any() == False or matriz2.any() == False:
            print("La partida termino, la victoria es para:", self.texto[self.turnoactual])
            self.victoria = True

    def cambiopeon(self):
        if self.pactual == Peon and self.plz[1] == 0:
            while True:
                print("Puedes cambiar tu peon por cualquiera de las piezas salvo el rey, escoje una!")
                respuesta = input("P R B N Q?\n").upper()
                if respuesta in "PRBNQ":
                    break
                else:
                    print("Ingrese un valor valido")
            pieza =  self.turnoactual + respuesta
            self.tablero.MD(self.plz, pieza)

    def seleccionador_(self):
        PD = {"P": Peon, "R": Torre, "B": Alfil, "N": Caballo, "Q": Reina, "K": Rey}
        seleccionada = PD.get(self.coo[0])
        self.pactual = seleccionada

    def run(self):
        while not self.victoria:
            self.tablero.display()
            print("Ahora es el turno de:", self.texto[self.turnoactual])
            self.turno()
            self.cambiopeon()
            self.checklose()
            self.__switchturn()


test = Ajedres()
test.run()
