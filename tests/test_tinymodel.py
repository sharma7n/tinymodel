from tinymodel import *
from .utils import *

@model
class TinyClass:
    """ Sample model class. """
    
    key_field = 'code'
    
    def __init__(self, *, code=None, attrib=False):
        self.code = code
        self.attrib = attrib
        
    def __repr__(self):
        return '<{cls} {attrs} at {id}>'.format(
            cls=self.__class__.__name__,
            attrs=self.__dict__,
            id=id(self))
    
    def __eq__(self, other):
        assert isinstance(other, self.__class__)
        return self.code, self.attrib == other.code, other.attrib

table = db.table('TinyClass')

def test_model_decorator():
    assert TinyClass.is_tinymodel
    assert TinyClass.__name__ == 'TinyClass'
    assert TinyClass.__doc__ == """ Sample model class. """

def test_connect():
    global db
    assert isinstance(db, TinyDB)

@rollback
def test_save():
    obj = TinyClass(code="test")
    save(obj)
    res = table.all()
    assert len(res) == 1
    assert obj.asdict() == res[0]

@rollback
def test_load():
    obj = TinyClass(code="test")
    table.insert(obj.asdict())
    res = list(load(TinyClass))
    assert len(res) > 0
    assert obj == res[0]