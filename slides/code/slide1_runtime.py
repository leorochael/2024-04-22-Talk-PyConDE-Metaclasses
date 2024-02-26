print("*** Antes da constante", list(globals()), sep='\n')

CONSTANTE = "valor"

print("*** Antes da classe", list(globals()), sep='\n')


class Pato:

    print("*** No começo da declaração da Classe", list(globals()), sep='\n')

    def __init__(self):
        print("*** Durante o init da instância", list(globals()), sep='\n')

    def quack(self):
        print("Quack!")

    print("*** No fim da declaração da classe", list(globals()), sep='\n')


print("*** Depois da classe", list(globals()), sep='\n')
