from tinydb import TinyDB, Query

from tinymodel import connect

db = connect("test.json")

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