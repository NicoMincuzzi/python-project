# python-project

## Dependencies

### `requirements.txt`
- Insert all dependencies that you need inside the `requirements.txt` file, as following:
  ```
  ```
- Create a virualenv and run it:
  1. `virtualenv venv`
  2. `source venv/bin/activate`
 
- Install dependencies:
  `pip install -r requirements.txt`

### `setuptools` and `setup.py`

- Setting up `setup.py`

### [Poetry](https://github.com/python-poetry/poetry)

- Prerequisites:

  * Install [pyenv](https://github.com/pyenv/pyenv#installation), which lets you easily switch between multiple versions of Python. In alternatives, you can use [pyenv-installer](https://github.com/pyenv/pyenv-installer)

  * Install [Poetry](https://github.com/python-poetry/poetry#installation), which is a tool for dependency management and packaging in Python. 

- Introduction
  
  `poetry` only needs one file to do all of that: the new, [standardized](https://www.python.org/dev/peps/pep-0518/) `pyproject.toml`.

  In other words, poetry uses `pyproject.toml` to replace `setup.py`, `requirements.txt`, `setup.cfg`, `MANIFEST.in` and the newly added `Pipfile`.

## Artifacts
