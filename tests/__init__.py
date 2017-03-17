from unittest import TestCase

from tinymodel import *


class TinyModelTest(TestCase):
    def setUp(self):
        connect("test.json")
    
    def tearDown(self):
        db.purge_tables()
        db.purge()