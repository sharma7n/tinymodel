from tinydb import TinyDB, Query


def tinymodel(cls):
    """ 
        Class decorator granting tinymodel API compatibility.
        Only classes that have pure **kwargs constructors are supported.
    """
    
    class TinyModel(cls):
        """ Subclass of cls with dict serialization and deserialization methods. """
        
        _tinymodel = True
        
        def asdict(self):
            """ Serializes object into a Python dictionary. """
            pass
        
        @classmethod
        def fromdict(cls, dict_):
            """ Deserializes object from a Python dictionary. """
            pass
    
    TinyModel.__name__ = cls.__name__
    return TinyModel