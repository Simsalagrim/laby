# Laby

> Laby video game

The idea is to recreat a labyrinth game in Pygame with Python3.6
Controls are keyboard arrows
All the needs for further developpement are listed in TODO_laby_dev.txt

## Setup

### Install the appropriate Python version (do this once)

Using [pyenv](https://github.com/pyenv/pyenv) (tool that helps you manage different Python version):
```
$ pyenv install -v 3.6.1
```

### Isolate your project to prevent Python version conflicts (do this once)

Using [virtualenv](https://virtualenv.pypa.io/en/stable/) (tool that prevents Python version and dependencies conflicts):

```
$ virtualenv -p <path-to-python> .venv
```

Note : replace `<path-to-python>` with the path to the `Python@3.6.1` binary. When installed with `pyenv`, the binary is located at `~/.pyenv/versions/3.6.1/bin/python3.6`

## Getting started

### Activate virtualenv

Always activate your `virtualenv` when moving to this project directory:

```
$ source .venv/bin/activate
```

Once done with your work, deactivate the virtualenv:

```
$ deactivate
```

### Start

```
$ python start.py
```

## Notes

Feel free to help!