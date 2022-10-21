
def __repr__(self):
    attr_repr = ', '.join(
        f'{name}={value!r}'
        for name, value in self.__dict__.items()
    )
    cls = self.__class__
    return f'{cls.__name__}({attr_repr})'


def add_repr(cls):
    cls.__repr__ = __repr__
    return cls


@add_repr
class MinhaClasse:

    def __init__(self, valor):
        self.valor = valor


m = MinhaClasse(valor=27)
