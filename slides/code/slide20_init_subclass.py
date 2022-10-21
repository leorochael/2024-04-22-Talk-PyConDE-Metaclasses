
ANSERIFORMES_VALIDOS = {
    'Pato',
    'Ganso',
    'Marreco',
    'Cisne',
}


class Anseriforme:

    def __init_subclass__(subclass):
        name = subclass.__name__
        if name not in ANSERIFORMES_VALIDOS:
            raise RuntimeError(
                f"{name} não é suficientemente patético"
            )
