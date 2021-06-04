# python-project

## Dependencies

### Install a package using `requirements.txt`
- Insert all dependencies that you need inside the `requirements.txt` file, as following:
  ```
  ```
- Create a virualenv and run it:
  1. `virtualenv venv`
  2. `source venv/bin/activate`
 
- Install dependencies:
  `pip install -r requirements.txt`

### Install a package using `setuptools` and `setup.py`

- Setting up `setup.py`

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
