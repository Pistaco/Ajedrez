from ajedrez import Ajedres

with open("Archivo/Convencion.txt", "r") as txt:
    print(txt.read())
input("Presiona una tecla para continuar")

test = Ajedres()
test.run()