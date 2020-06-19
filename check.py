
class Check:
    """
    Verificar todos los parametros y arrojarlos a main()
    """
    def __init__(self, ai):
        self.rows = list("ABCDEFGH")
        self.columns = list("12345678")
        self.tablero = ai.tablero

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
                elif valor[0].upper() not in "KQRBNP":
                    print("pieza no valida")           # 4)
                else:
                    return valor
            else:
                print("Demasiado largo")

    def run(self):
        """Funcion que se ejecuta en main(), pregunta por la informacion y la transforma a coordenadas.

        Te traduce a formato que te pueda entender el index del tablero

        Tranformador de formato:
        ABCDEFGH -> 012345678
        str -> int
        lowercase -> UPPERCASE

        Te arroja las tuplas correspondientes
        """
        pieza, row, column = self.input_("Que pieza desea mover?\n")
        piezaB, rowB, columnB = self.input_("Hacia donde desea moverla?\n")
        tupla1 = (pieza.upper(), self.rows.index(row.upper()), self.columns.index(column))
        tupla2 = (piezaB.upper(), self.rows.index(rowB.upper()), self.columns.index(columnB))
        print(tupla1, tupla2)
        return tupla1, tupla2

    def check_get(self, origen, destino):
        get1 = self.tablero.GET(origen)
        get2 = self.tablero.GET(destino)

        def check_pieza(evaluar):
            if get1[1] == evaluar and get2[1] == evaluar:
                return True
