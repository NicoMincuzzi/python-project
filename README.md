# python-project

## Dependencies

### Install a package using `requirements.txt`
- Insert all dependencies that you need inside the `requirements.txt` file, as following:
  
  ```
  Flask==1.1.2
  ```
  
- Set up a virtual environment:
  
  ``` sh
  $ virtualenv venv
  ```
  
  This will create a new virtual environment named venv using the version of Python that you have installed on your system.
  
- Activate the virtual environment by sourcing the activation script:
  
  ``` sh
  $ source venv/bin/activate
  ```
  
  After executing this command, your prompt will change to indicate that you’re now operating from within the virtual environment.
 
- Install all dependencies:
  
  ``` sh
  $ pip install -r requirements.txt
  ```

### Install a package using `setuptools` and `setup.py`

Create the following project structure:

  ```
  python-demo
  ├── README.md
  ├── LICENSE
  ├── setup.py
  ├── package_demo
  │   └── __init__.py
  └── tests
      ├── __init__.py
      └── test_python_demo.py
  ```
The contents of setup.py is just pure python:
  ``` python
  import os
  from setuptools import setup

  # Utility function to read the README file.
  # Used for the long_description.  It's nice, because now 1) we have a top level
  # README file and 2) it's easier to type in the README file than to put a raw
  # string in below ...
  def read(fname):
      return open(os.path.join(os.path.dirname(__file__), fname)).read()

  setup(
      name = "an_example_pypi_project",
      version = "0.0.4",
      author = "Andrew Carter",
      author_email = "andrewjcarter@gmail.com",
      description = ("An demonstration of how to create, document, and publish "
                                     "to the cheese shop a5 pypi.org."),
      license = "BSD",
      keywords = "example documentation tutorial",
      url = "http://packages.python.org/an_example_pypi_project",
      packages=['an_example_pypi_project', 'tests'],
      long_description=read('README'),
      classifiers=[
          "Development Status :: 3 - Alpha",
          "Topic :: Utilities",
          "License :: OSI Approved :: BSD License",
      ],
  )
  ```

Using setup.py
The basic usage of setup.py is:
``` sh
$ python setup.py <some_command> <options>
```
To see all commands type:
``` sh
$ python setup.py --help-commands
```
And you will get:
```
Standard commands:
  build             build everything needed to install
  build_py          "build" pure Python modules (copy to build directory)
  build_ext         build C/C++ extensions (compile/link to build directory)
  build_clib        build C/C++ libraries used by Python extensions
  build_scripts     "build" scripts (copy and fixup #! line)
  clean             clean up temporary files from 'build' command
  install           install everything from build directory
  install_lib       install all Python modules (extensions and pure Python)
  install_headers   install C/C++ header files
  install_scripts   install scripts (Python or otherwise)
  install_data      install data files
  sdist             create a source distribution (tarball, zip file, etc.)
  register          register the distribution with the Python package index
  bdist             create a built (binary) distribution
  bdist_dumb        create a "dumb" built distribution
  bdist_rpm         create an RPM distribution
  bdist_wininst     create an executable installer for MS Windows
  upload            upload binary package to PyPI

Extra commands:
  rotate            delete older distributions, keeping N newest files
  develop           install package in 'development mode'
  setopt            set an option in setup.cfg or another config file
  saveopts          save supplied options to setup.cfg or other config file
  egg_info          create a distribution's .egg-info directory
  upload_sphinx     Upload Sphinx documentation to PyPI
  install_egg_info  Install an .egg-info directory for the package
  alias             define a shortcut to invoke one or more commands
  easy_install      Find/get/install Python packages
  bdist_egg         create an "egg" distribution
  test              run unit tests after in-place build
  build_sphinx      Build Sphinx documentation

usage: setup.py [global_opts] cmd1 [cmd1_opts] [cmd2 [cmd2_opts] ...]
   or: setup.py --help [cmd1 cmd2 ...]
   or: setup.py --help-commands
   or: setup.py cmd --help
```

### Poetry

- **Prerequisites**

  * Install [pyenv](https://github.com/pyenv/pyenv#installation), which lets you easily switch between multiple versions of Python. In alternatives, you can use [pyenv-installer](https://github.com/pyenv/pyenv-installer)

  * Install [Poetry](https://github.com/python-poetry/poetry#installation), which is a tool for dependency management and packaging in Python. 

- **Introduction**
  
  `poetry` only needs one file to do all of that: the new, [standardized](https://www.python.org/dev/peps/pep-0518/) `pyproject.toml`.

  In other words, poetry uses `pyproject.toml` to replace `setup.py`, `requirements.txt`, `setup.cfg`, `MANIFEST.in` and the newly added `Pipfile`.

- **Project setup**
  
  First, let's create our new project, let's call it `poetry-demo`:

  `poetry new poetry-demo`

  This will create the `poetry-demo` directory with the following content:
  
  ```
  poetry-demo
  ├── pyproject.toml
  ├── README.rst
  ├── poetry_demo
  │   └── __init__.py
  └── tests
      ├── __init__.py
      └── test_poetry_demo.py
  ```

  The `pyproject.toml` file is what is the most important here. This will orchestrate your project and its dependencies. For now, it looks like this:

  ```
  [tool.poetry]
  name = "poetry-demo"
  version = "0.1.0"
  description = ""
  authors = ["Sébastien Eustace <sebastien@eustace.io>"]

  [tool.poetry.dependencies]
  python = "*"

  [tool.poetry.dev-dependencies]
  pytest = "^3.4"
  ```

## Artifacts
