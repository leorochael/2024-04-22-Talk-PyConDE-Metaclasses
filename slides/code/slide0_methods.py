
class MinhaClasse:

    x = 42

    def dobrar(self):
        return self.x * 2


class MinhaSubClasse(MinhaClasse):

    x = 36

    def __repr__(self):
        return f'<MinhaSubClasse x={self.x}>'

