from tinydb import TinyDB, Query

from tinymodel import *


db = connect("tests/test.json")
    
def rollback(test_func):
    """ 
        Simple decorator that cleans the passed-in database at the end.
        Ensures that each unit test is independent.
    """
    
    def with_rollback(*args, **kwargs):
        global db
        try:
            test_func(*args, **kwargs)
        finally:
            db.purge_tables()
            db.purge()
    return with_rollback

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
    print(obj)
    print(res[0])
    print(obj.code, obj.attrib)
    print(res[0].code, res[0].attrib)
    print(obj.__eq__(res[0]))
    assert obj == res[0]