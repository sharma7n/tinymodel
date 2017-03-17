# tinymodel
A wrapper around TinyDB for easy JSON serialization and deserialization.

# Quickstart

```python
from tinymodel import tinymodel, connect, save, load

connect("path/to/file.json")

@tinymodel
class MyClass:
    def __init__(self, *, foo=False):
        self.foo = foo

myobject1 = MyClass()
myobject2 = MyClass(foo=True)
save(myobject1)
save(myobject2)

for o in load(MyClass):
    print(o.foo)

>> False
>> True
```