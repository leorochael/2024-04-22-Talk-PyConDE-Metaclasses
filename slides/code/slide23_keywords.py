
from slide12_walkthru import MetaAnseriforme

print("# antes da classe com __init_subclass__")

class Cisne(metaclass=MetaAnseriforme):

    def __init_subclass__(subclass, **kw):
      print("consumindo", kw)
      super().__init_subclass__(subclass)

print("# entre a classe com __init_subclass__ e a subclasse")

class CisneNegro(Cisne, palavra="chave"):
    pass

print(f"# fim do módulo {__name__}")
