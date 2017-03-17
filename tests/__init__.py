from unittest import TestCase

from tinydb import Query

from tinymodel import *


class TinyModelTest(TestCase):
    def setUp(self):
        self.db = connect("test.json")
        
        @tinymodel
        class TestClass:
            key_field = 'code'
            
            def __init__(self, *, code=None, attrib=False):
                self.code = code
                self.attrib = attrib
                
            def __repr__(self):
                '<{cls} {attrs} at {id}>'.format(
                    cls=self.__class__.__name__,
                    attrs=self.__dict__,
                    id=id(self))

            def __eq__(self, other):
                return self.code == other.code and self.attrib == other.attrib
        
        self.TestClass = TestClass
        self.obj = TestClass(code="test")
    
    def test_tinymodel_has_asdict(self):
        assert hasattr(self.obj, 'asdict')
        
    def test_tinymodel_has_fromdict(self):
        assert hasattr(self.TestClass, 'fromdict')
        
    def test_asdict(self):
        assert self.obj.asdict() == {'code': "test", 'attrib': False}
        
    def test_fromdict(self):
        obj_from_dict = self.TestClass.fromdict({'code': "test2", 'attrib': True})
        obj_from_init = self.TestClass(code="test2", attrib=True)
        assert obj_from_dict == obj_from_init
        
    def tearDown(self):
        self.db.purge_tables()
        self.db.purge()