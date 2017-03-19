# tinymodel
![Travis CI](https://travis-ci.org/sharma7n/tinymodel.svg?branch=master)

A wrapper around TinyDB for easy JSON serialization and deserialization.

# Quickstart

```python
from tinymodel import model, connect, save, load

connect("path/to/file.json")

@model
class MyClass:
    def __init__(self, *, foo=False):
        self.foo = foo

>> obj = MyClass()
>> save(obj)
>> for o in load(MyClass):
>>    print(o.foo)
False
```