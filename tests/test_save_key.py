from tinymodel import *
from .utils import *

@model
class KeyClass:
    def __init__(self, key):
        self.key = key

key_table = db.table('KeyClass')

@rollback
def test_save_same_key():
    a = KeyClass("a")
    save(a)
    
    a2 = KeyClass("a")
    save(a2)
    
    res = key_table.all()
    assert len(res) == 1
    assert a.asdict() == res[0]

    
@rollback
def test_save_different_key():
    a = KeyClass("a")
    save(a)
    
    b = KeyClass("b")
    save(b)
    
    res = key_table.all()
    assert len(res) == 2


@model
class CustomKeyClass:
    key_field = 'name'
    
    def __init__(self, name):
        self.name = name

custom_key_table = db.table('CustomKeyClass')

@rollback
def test_save_same_custom_key():
    a = CustomKeyClass("a")
    save(a)
    
    a2 = CustomKeyClass("a")
    save(a2)
    
    res = custom_key_table.all()
    assert len(res) == 1
    assert a.asdict() == res[0]


@rollback
def test_save_different_custom_key():
    a = CustomKeyClass("a")
    save(a)
    
    b = CustomKeyClass("b")
    save(b)
    
    res = custom_key_table.all()
    assert len(res) == 2

@model
class NoKeyClass:
    def __init__(self, nokey):
        self.nokey = nokey

no_key_table = db.table('NoKeyClass')

@rollback
def test_save_same_no_key():
    a = NoKeyClass("a")
    save(a)
    
    a2 = NoKeyClass("a")
    save(a2)
    
    res = no_key_table.all()
    assert len(res) == 2
    assert a.asdict() == res[0]
    
@rollback
def test_save_different_no_key():
    a = NoKeyClass("a")
    save(a)
    
    b = NoKeyClass("b")
    save(b)
    
    res = no_key_table.all()
    assert len(res) == 2