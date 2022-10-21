class MetaAnseriforme(type):

    def __init__(cls, cls_name, bases, cls_dict, **kw):
        print(f'** __init__ da metaclasse para', cls_name)
        super().__init__(cls_name, bases, cls_dict, **kw)

    def __repr__(cls):
        cls_name = cls.__name__
        return f"<Classe para fazer {cls_name!r}>"


class Anseriforme(metaclass=MetaAnseriforme):

    registro = {}

    def __init_subclass__(subclass):
        print(f'** registrando', subclass.__name__)
        subclass.registro[subclass.__name__] = subclass

    def __class_getitem__(cls, name):
        return cls.registro[name]


ANSERIFORMES_VALIDOS = {
    'Pato',
    'Ganso',
    'Marreco',
    'Cisne',
}

def verifica_anseriforme(cls):
    print("** verificando:", cls.__name__)
    name = cls.__name__
    if name not in ANSERIFORMES_VALIDOS:
        raise RuntimeError(
            f"{name} não é suficientemente patético"
        )


@verifica_anseriforme
class Pato(Anseriforme):

    def quack(self):
        print("Quack!")
