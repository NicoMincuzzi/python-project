# python-project

## Install a package using `requirements.txt`
- Insert all dependencies that you need inside the `requirements.txt` file, for example as following:
  
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

## Install a package using `setuptools` and `setup.py`

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
  ```python
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

You have most likely used a requirements.txt file before. Now that you are creating a setup.py, you can specify your
dependencies in the `install_requires argument`. For example, in a project you may have:

```python
setup(
    ...
    install_requires=[
        'PyYAML',
        'pandas==0.23.3',
        'numpy>=1.14.5',
        'matplotlib>=2.2.0,,
        'jupyter'
    ]
)
```

You may specify requirements without a version (PyYAML), pin a version (pandas==0.23.3), specify a minimum version ('numpy>=1.14.5) or set a range of versions (matplotlib>=2.2.0,<3.0.0). These requirements will automatically be installed by pip when you install your package.

## Poetry

## Prerequisites

  * Install [pyenv](https://github.com/pyenv/pyenv#installation)
    - which lets you easily switch between multiple versions of Python. In alternatives, you can use [pyenv-installer](https://github.com/pyenv/pyenv-installer)

  * Install [Poetry](https://github.com/python-poetry/poetry#installation)
    - tool for dependency management and packaging in Python. 

## Introduction
  
  `poetry` only needs one file to do all of that: the new, [standardized](https://www.python.org/dev/peps/pep-0518/) `pyproject.toml`.

  In other words, poetry uses `pyproject.toml` to replace `setup.py`, `requirements.txt`, `setup.cfg`, `MANIFEST.in` and the newly added `Pipfile`.

## Project setup
  
  First, let's create our new project, let's call it `poetry-demo`:

  `$ poetry new poetry-demo`

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
  
### Initialising a pre-existing project
  
Instead of creating a new project, Poetry can be used to *'initialise'* a pre-populated directory. To interactively create a `pyproject.toml` file in directory pre-existing-project:

  ``` sh
  cd pre-existing-project
  $ poetry init
  ```

### Specifying dependencies

If you want to add dependencies to your project, you can specify them in the `tool.poetry.dependencies` section.

```
[tool.poetry.dependencies]
pendulum = "^1.4"
```

Poetry uses this information to search for the right set of files in package "repositories" that you register in the `tool.poetry.repositories` section, or on PyPI by default.

Also, instead of modifying the `pyproject.toml` file by hand, you can use the add command.

``` sh
$ poetry add pendulum
```

It will automatically find a suitable version constraint and install the package and subdependencies.

## Using your virtual environment

By default, poetry creates a virtual environment in `{cache-dir}/virtualenvs` (`{cache-dir}\virtualenvs` on Windows). You can change the `cache-dir` value by editing the poetry config. Additionally, you can use the `virtualenvs.in-project` configuration variable to create virtual environment within your project directory.

```sh
$ poetry config virtualenvs.in-project true
```

There are several ways to run commands within this virtual environment.

### Using poetry `run`
To run your script simply use `$ poetry run python your_script.py`. Likewise if you have command line tools such as `pytest` or `black` you can run them using `$ poetry run pytest`.

### Activating the virtual environment
The easiest way to activate the virtual environment is to create a new shell with poetry shell. To deactivate the virtual environment and exit this new shell type exit. To deactivate the virtual environment without leaving the shell use deactivate.

## Installing dependencies
To install the defined dependencies for your project, just run the `install` command.

``` sh
$ poetry install
```

When you run this command, one of two things may happen:

- ### Installing without poetry.lock
If you have never run the command before and there is also no poetry.lock file present, Poetry simply resolves all dependencies listed in your pyproject.toml file and downloads the latest version of their files.

When Poetry has finished installing, it writes all of the packages and the exact versions of them that it downloaded to the poetry.lock file, locking the project to those specific versions. You should commit the poetry.lock file to your project repo so that all people working on the project are locked to the same versions of dependencies (more below).

- ### Installing with poetry.lock
This brings us to the second scenario. If there is already a poetry.lock file as well as a pyproject.toml file when you run poetry install, it means either you ran the install command before, or someone else on the project ran the install command and committed the poetry.lock file to the project (which is good).

Either way, running install when a poetry.lock file is present resolves and installs all dependencies that you listed in pyproject.toml, but Poetry uses the exact versions listed in poetry.lock to ensure that the package versions are consistent for everyone working on your project. As a result you will have all dependencies requested by your pyproject.toml file, but they may not all be at the very latest available versions (some of the dependencies listed in the poetry.lock file may have released newer versions since the file was created). This is by design, it ensures that your project does not break because of unexpected changes in dependencies.

- ### Commit your poetry.lock file to version control
Committing this file to VC is important because it will cause anyone who sets up the project to use the exact same versions of the dependencies that you are using. Your CI server, production machines, other developers in your team, everything and everyone runs on the same dependencies, which mitigates the potential for bugs affecting only some parts of the deployments. Even if you develop alone, in six months when reinstalling the project you can feel confident the dependencies installed are still working even if your dependencies released many new versions since then. (See note below about using the update command.)

**N.B.** For libraries it is not necessary to commit the lock file.
