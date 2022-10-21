
class MinhaClasse:

    x = 42

    def dobrar(self):
        return self.x * 2


class MeuMixin:

    def somar(self):
        return self.x + 2


class MinhaSubClasse(MinhaClasse, MeuMixin):

    x = 36


def meu_gerador_de_subclasse(novo_x):

    class MinhaSubClasseDinamica(MinhaClasse, MeuMixin):

        x = novo_x

    return MinhaSubClasseDinamica