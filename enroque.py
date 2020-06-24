class Enroque:
    def __init__(self, ai):
        self.enroquenegras = [0, 0, 0, 0]
        self.enroqueblancas = [0, 0, 0, 0]
        self.largo = [4, 5, 6]
        self.corto = [1, 2]
        self.rows = {"W": 7, "B": 0}
        self.tablero = ai.Tablero

    def colisionador(self, opcion, ta):
        self.row = self.rows[ta]

        if opcion == "**":
            lista = self.tablero.data[self.row, self.largo] == ""
        else:
            lista = self.tablero.data[self.row, self.corto] == ""
        if lista.all():
            print("Enroque exitoso")
            return True
        else:
            print("No se puede realizar el enroque, existen piezas estorbando")
            return False

    def enroque(self, valor):
        def translate(origen, destino):
            self.tablero.data[self.row, origen], self.tablero.data[self.row, destino] =\
                self.tablero.data[self.row, destino], self.tablero.data[self.row, origen]
        if valor == "**":
            translate(3, 5)  # Rey
            translate(7, 4)  # Torre
        elif valor == "*":
            translate(3, 1)  # Rey
            translate(0, 2)  # Torre

    def contador(self, coo, ta):
        if ta == "W":
            lista = self.enroqueblancas
        else:
            lista = self.enroquenegras

        if coo[2] == 0 and not lista[0]:
            lista[0] = 1
        elif coo[2] == 7 and not lista[2]:
            lista[2] = 1
        elif not lista[1]:
            lista[1] = 1
        else:
            print("ERROR")
            raise

    def contador2(self, ta):
        if ta == "W":
            if not self.enroqueblancas[3]:
                self.enroqueblancas[3] = 1
        else:
            if not self.enroquenegras[3]:
                self.enroquenegras[3] = 1

