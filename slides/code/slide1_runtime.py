print("*** Antes da constante", list(globals()))

CONSTANTE = "valor"

print("*** Antes da classe", list(globals()))


class Pato:

    print("*** No começo da declaração da Classe", list(globals()))

    def __init__(self):
        print("*** Durante o init da instância", list(globals()))

    def quack(self):
        print("Quack!")

    print("*** No fim da declaração da classe", list(globals()))


print("*** Depois da classe", list(globals()))
