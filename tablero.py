class Tablero:
    """Clase cuya unica funcion es manejar los datos del tablero.
    """

    def __init__(self):
        """Crear el diccionario de datos.

        Letras: row
        Numeros: column
        """

        self.data = [
            ["BR", "BB", "BN", "BK", "BQ", "BN", "BB", "BR"],
            ["BP", "BP", "BP", "BP", "BP", "BP", "BP", "BP"],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["WP", "WP", "WP", "WP", "WP", "WP", "WP", "WP"],
            ["WR", "WB", "WN", "WK", "WQ", "WN", "WB", "WR"]
        ]

        self.keys = tuple("ABCDEFGH")
    def display(self):
        """
        Mostrar el tablero en pantalla.
        """

        print("     (#1) (#2) (#3) (#4) (#5) (#6) (#7) (#8)")
        for x, k in enumerate(self.data):
            valores = ""
            for V in k:
                if V:
                    valores = f"{valores} [{V}]"
                else:
                    valores = f"{valores} [  ]"
            print(f"({self.keys[x]}) {valores}")

    def MD(self, origen, objeto):
        """Funcion que te permite modificar el diccionario del tablero.

        El primer parametro debe estar en el formato de coordenadas (P: Pieza, G: Row, 1: Column) y ademas tener
        siempre una longitud de 3, de lo contrario arrojara error 
        El segundo parametro  debe ser lo que desees sobrescribir

        """
        row, columna = origen[1:]
        self.data[row][columna] = objeto

    def GET(self, origen, bol: bool = False):
        """Funcion que te permite obtener una valor del tablero.
        origen = coordenadas
        bol = el valor lo puedes tener en bool
        """
        row, columna = origen[1:]
        data = self.data[row][columna]
        if bol:
            return bool(data)
        return data
