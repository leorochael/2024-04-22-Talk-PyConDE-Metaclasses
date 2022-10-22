class AutoStringDict(dict):

    def __missing__(self, key: str):
        if key.startswith('__') and key.endswith('__'):
            # pula attributos/metodos especiais
            raise KeyError(key)

        # cria a chave e o valor automaticamente.
        self[key] = key.capitalize()
        return key


class AutoStringMeta(type):
    def __prepare__(name, bases, **kwargs):
        return AutoStringDict()


class AutoString(metaclass=AutoStringMeta):
    pass
