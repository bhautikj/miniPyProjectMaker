# TEMPLATE

## About
TEMPLATE package that does something

## Installing
```console
$ pip install .
```

## Usage
```python
>>> import TEMPLATE
>> TEMPLATE.DummySpit()
'BLARGH'
>>> import TEMPLATE.core.base
>>> TEMPLATE.core.base.DummySpit()
'BLARGH_BASE'
```

## Runing tests:

```console
$ python setup.py test
running test
running egg_info
creating TEMPLATE.egg-info
writing TEMPLATE.egg-info/PKG-INFO
writing dependency_links to TEMPLATE.egg-info/dependency_links.txt
writing top-level names to TEMPLATE.egg-info/top_level.txt
writing manifest file 'TEMPLATE.egg-info/SOURCES.txt'
reading manifest file 'TEMPLATE.egg-info/SOURCES.txt'
writing manifest file 'TEMPLATE.egg-info/SOURCES.txt'
running build_ext
test_base (TEMPLATE.tests.test_base.TestBase) ... ok
test_root (TEMPLATE.tests.test_base.TestBase) ... ok

----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK
```

^`Built using [miniPyProjectMaker](https://github.com/bhautikj/miniPyProjectMaker)`^