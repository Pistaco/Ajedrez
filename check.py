
class Check:
    """
    Verificar todos los parametros y arrojarlos a main()
    """
    def __init__(self, ai):
        self.check = False
        self.rows = list("ABCDEFGH")
        self.columns = list("12345678")
        self.tablero = ai.tablero
        self.ta = ai.turnoactual

    def input_(self, pregunta):
        """Verifica coordenadas tanto de origen como de destino, no hace cambios en los datos, solo los checkea.

           Primero se encarga del input, seguido lo ingresa a un bucle y no sale hasta que cumpla los parametros:
        1) Verifica si el tamaño del input es 3
        2) Verifica si el row esta entre los valores permitidos
        3) Verifica si la column esta entre los valores permitidos
        4) Verifica si la pieza existe"""

        while True:
            valor = input(pregunta)
            if len(valor) == 3:  # 1)
                if valor[1].upper() not in self.rows:  # 2)
                    print("Row incorrecta")
                elif valor[2] not in self.columns:  # 3)
                    print("columna incorrecta")
                elif valor[0] not in "KQRBNP":
                    print("pieza no valida")           # 4)
                else:
                    return valor

    def info(self):
        """Pregunta por la informacion y la transforma a coordenadas.


        Tranformador de formato:
        ABCDEFGH -> 012345678
        str -> int
        lowercase -> UPPERCASE
        """
        pieza, row, column = self.input_("Que pieza desea mover?\n")
        piezaB, rowB, columnB = self.input_("Hacia donde desea moverla?\n")
        tupla1 = (pieza.upper(), self.rows.index(row.upper()), self.columns.index(column))
        tupla2 = (piezaB.upper(), self.rows.index(rowB.upper(), self.columns.index(columnB)))
        return tupla1, tupla2

    def run(self):
        """Todos los procesos en conjunto.

        4) Pieza
        5) Turno
        """
        while True:
            coo, poo = self.info()
            get1 = self.tablero.GET(coo)
            get2 = self.tablero.GET(poo)
            if get1[0] != self.ta and get2[0] != self.ta:
                print("No es tu turno para mover esta pieza")
            elif get1[1] != coo[0] and get2[1] != poo[0]:
                print("La pieza no coincide con el tablero")
            else:
                break