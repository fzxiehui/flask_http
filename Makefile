.PHONY: help test venv install build run migrate

default: help

VENV = venv
PYTHON = $(VENV)/bin/python
PIP = $(VENV)/bin/pip
PYTEST = $(VENV)/bin/pytest

help:
	@echo "help"

venv:
	python -m venv $(VENV)
	echo "*" > $(VENV)/.gitignore

install:
	$(PIP) install -r requirements.txt

build:
	-rm build/ -rf 
	-rm dist/ -rf
	$(PYTHON) setup.py sdist bdist_wheel

run:
	$(PYTHON) main.py

test:
	$(PIP) install -e .
	$(PYTEST) -s	

migrate:
	$(VENV)/bin/flask db init
	$(VENV)/bin/flask db migrate -m "init tables"
	$(VENV)/bin/flask db upgrade
