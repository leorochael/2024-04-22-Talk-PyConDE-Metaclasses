class better_repr_type(type):

    def __init__(cls, name, bases, namespace_dict):

        # self is a new class

        def __repr__(self):
            attr_repr = ', '.join(
                f'{name}={value!r}'
                for name, value in self.__dict__.items()
            )
            cls = self.__class__
            return f'{cls.__name__}({attr_repr})'

        # Injetando método na classe para uso da instância:
        cls.__repr__ = __repr__

    # Método para uso da classe
    def __repr__(cls):
        bases = ', '.join(c.__name__ for c in cls.__bases__)
        return f'{cls.__name__}({bases})'

    x = 25
