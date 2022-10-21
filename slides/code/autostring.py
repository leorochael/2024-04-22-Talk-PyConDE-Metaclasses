class AutoStringDict(dict):

    def __missing__(self, key):
        if key.startswith('__') and key.endswith('__'):
            raise KeyError(key)
        # autocreate the key
        self[key] = key
        return key

class AutoStringMeta(type):
    def __prepare__(name, bases, **kwargs):
        return AutoStringDict()

class AutoString(metaclass=AutoStringMeta):
    pass
