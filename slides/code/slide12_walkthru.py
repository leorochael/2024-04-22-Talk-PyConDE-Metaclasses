print('* Início do módulo {__name__}')

from collections import UserDict

class LogDict(UserDict):
    def __setitem__(self, key, item):
        print("*** novo atributo", key)
        return super().__setitem__(key, item)


class MetaAnseriforme(type):
    print('** Início da metaclasse')

    @classmethod
    def __prepare__(metacls, cls_name, cls_bases, **kw):
        print("*** preparando o namespace da classe")

        def debug(msg):
            print(f"** na classe:", cls_name, "mensagem:", msg)

        cls_dict = LogDict({'debug': debug})
        return cls_dict

    def __new__(meta_cls, cls_name, bases, cls_dict, **kw):
        print(f'*** __new__ da metaclasse')

        cls_dict = dict(cls_dict)
        del cls_dict['debug']
        cls = super().__new__(meta_cls, cls_name, bases, cls_dict, **kw)

        return cls

    def __init__(cls, cls_name, bases, cls_dict, **kw):
        print(f'*** __init__ da metaclasse')
        super().__init__(cls_name, bases, cls_dict, **kw)

    def __call__(cls):
        print('*** __call__ da metaclasse')
        return super().__call__()

    def __repr__(cls):
        cls_name = cls.__name__
        return f"<Classe {cls_name!r} com repr MetaAnseriforme>"

    print('** Fim da metaclasse')


print('* Entre metaclasse e classe')


class Pato(metaclass=MetaAnseriforme):

    debug("No começo da declaração da classe")

    def __new__(cls):
        print("*** Durante o __new__ da classe")
        return super().__new__(cls)

    def __init__(self):
        print("*** Durante o init da classe")

    def quack(self):
        print("Quack!")

    debug("No fim da declaração da classe")


print('* Entre classe e subclasse')


class PatoMandarim(Pato):

    debug("declarando a subclasse")

    def quack(self):
        print("Qué!")

    debug("fim da declaração da subclasse")


print('* Entre subclasse e instância')

pato = Pato()

print(f'* Fim do módulo {__name__}')
