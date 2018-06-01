# miniPyProjectMaker

## About
This is a one-shot tool for creating a tiny, working python project written in the style of [`python-packaging`](http://python-packaging.readthedocs.io/en/latest/minimal.html). The packages have a `setup.py` that can be used to install the package via `pip` (I'd recommend combining this with a `virtualenv`-type setup). The projects it generates are flavored to favor my own peculiar brand of python module management.

## Getting it
```console
$ git clone https://github.com/bhautikj/miniPyProjectMaker
$ cd miniPyProjectMaker
```

## Creating a project
If we wanted to create a mininmal project called `foo`, use:
```console
$ python setup_project.py --name foo
```

`miniPyProjectMaker` will create a directory named `foo` and populates it with a minimal, `setup.py`-centric project which can later be installed using `pip`.

### What's in the project
```
foo/setup.py
foo/.gitignore
foo/README.md
foo/foo/__init__.py
foo/foo/core/__init__.py
foo/foo/core/base.py
foo/foo/tests/__init__.py
foo/foo/tests/test_base.py
```

I've included a couple of functions to get you started - `foo/foo/__init__.py` contains a dummy function to return a string:
```python
>>> import foo
>>> foo.DummySpit()
'BLARGH'
```

I've also included a sample module which can also be imported, and also contains a dummy function:
```python
>>> import foo.core.base
>>> foo.core.base.DummySpit()
'BLARGH_BASE'
```

There's also a default, python-centric `.gitignore` and a `README.md` to get you started.

### Testing
There are unit tests! Have a look in `foo/foo/tests/test_base.py`. You can run the tests with `python setup.py test`

```console
$ python setup.py test
running test
running egg_info
creating foo.egg-info
writing foo.egg-info/PKG-INFO
writing dependency_links to foo.egg-info/dependency_links.txt
writing top-level names to foo.egg-info/top_level.txt
writing manifest file 'foo.egg-info/SOURCES.txt'
reading manifest file 'foo.egg-info/SOURCES.txt'
writing manifest file 'foo.egg-info/SOURCES.txt'
running build_ext
test_base (foo.tests.test_base.TestBase) ... ok
test_root (foo.tests.test_base.TestBase) ... ok

----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK
```

## Options
```console
$ python setup_project.py -h
usage: setup_project.py [-h] [-n NAME] [-f]

Generate a minimal python project, bhautikj-style

optional arguments:
  -h, --help            show this help message and exit
  -n NAME, --name NAME  project to create
  -f, --force           force overwrite of existing project
```



