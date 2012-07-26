
class MetaGISProvider(type):
    registered_providers = []

    def __new__(mcs, name, bases, dct):
        # Name check for base class
        if name is  "BaseGISProvider":
            return type.__new__(mcs, name, bases, dct)

        if 'get_latlong' not in dct:
            raise AttributeError(
                    "get_latlong missing from '%s' class definition" % name)

        # List of providers (really for debugging)
        dct['__providers__'] = mcs.registered_providers

        ins = type.__new__(mcs, name, bases, dct)

        if 'priority' in dct and dct['priority'] >= 0:
            mcs.registered_providers.insert(dct['priority'], ins)
        else:
            mcs.registered_providers.append(ins)

        return ins

class BaseGISProvider(object):
    __metaclass__ = MetaGISProvider

    pass
