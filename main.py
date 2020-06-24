from piezas import Pieza, Peon, Torre, Alfil, Caballo, Reina, Rey
from tablero import Tablero
from check import Check
from enroque import Enroque

class Ajedres:
    def __init__(self):
        self.Tablero = Tablero()
        self.turnoactual = "W"
        self.Check = Check(self)
        self.Enroque = Enroque(self)
        self.texto = {"W": "Las blancas!", "B": "Las negras!"}
        self.victoria = False
        self.turno = False
        self.enroque = None
        self.oficial = None

    def __switchturn(self):
        if self.turnoactual == "W":
            self.turnoactual = "B"
        elif self.turnoactual == "B":

            self.turnoactual = "W"

    def check(self):
        while not self.turno:
            self.coo, self.plz = self.Check.run()
            self.checkenroque(self.coo)
            if self.oficial:
                self.seleccionador_(self.coo)
                if self.turno:
                    self.turno = self.pactual(self).accion()
                    self.ofical_run()
            elif self.enroque:
                self.enroque_run()
                self.turno = True

    def reset(self):
        self.enroque = None
        self.oficial = None
        self.turno = False

    def run(self):
        while not self.victoria:
            self.Tablero.display()
            print("Ahora es el turno de:", self.texto[self.turnoactual])
            self.check()
            self.reset()

    def ofical_run(self):
        self.cambiopeon()
        self.checklose()
        self.checkrk()
        self.__switchturn()

    def enroque_run(self):
        self.Enroque.enroque(self.coo)
        self.Enroque.contador2(self.turnoactual)
        self.__switchturn()

    def checkenroque(self, coo):
        if self.coo not in ("*", "**"):
            self.oficial = True
            self.enroque = False
            return False

        check = False
        if self.turnoactual == "W":
            lista = self.Enroque.enroqueblancas
        else:
            lista = self.Enroque.enroquenegras
        torre1, rey, torre2, enroque = lista
        if not enroque and not rey:
            if self.coo == "*" and not torre1:
                check = True
            elif self.coo == "**" and not torre2:
                check = True
            elif torre1:
                print("No puedes realizar enroque corto, ya moviste la torre")
            elif torre2:
                print("No puedes realizar enroque largo, ya moviste la torre")
        elif enroque:
            print("No puedes realizar enroque, ya lo hiciste con anterioridad")
        elif rey:
            print("No puedes realizar enroque, ya moviste al rey")
        if check:
            if self.Enroque.colisionador(coo, self.turnoactual):
                self.enroque = True
        else:
            self.enroque = False

    def checkrk(self):
        if self.pactual == Torre or self.pactual == Rey:
            self.Enroque.contador(self.coo, self.turnoactual)

    def checklose(self):
        matriz = self.Tablero.data == "WK"
        matriz2 = self.Tablero.data == "BK"
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
            self.Tablero.MD(self.plz, pieza)

    def seleccionador_(self, coo):
        PD = {"P": Peon, "R": Torre, "B": Alfil, "N": Caballo, "Q": Reina, "K": Rey}
        seleccionada = PD.get(coo[0])
        get = self.Tablero.GET(coo)
        if self.Check.check_p(coo[0], get):
            self.pactual = seleccionada
            self.turno = True
        else:
            self.turno = False

test = Ajedres()
test.run()
