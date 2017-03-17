from setuptools import setup

setup(name='tinymodel',
    version='0.1',
    description='A wrapper around TinyDB for easy JSON serialization and deserialization.',
    url='http://github.com/sharma7n/funniest',
    author='Nik Sharma',
    author_email='sharma7n@gmail.com',
    license='MIT',
    packages=['tinymodel'],
    install_requires=[
        'tinydb',
    ],
    zip_safe=False)