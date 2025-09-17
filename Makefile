.PHONY: help test venv install build run migrate

default: help

VENV = venv
PYTHON = $(VENV)/bin/python
PIP = $(VENV)/bin/pip
PYTEST = $(VENV)/bin/pytest

IMAGE_NAME = test-flask-app
VERSION ?= 1.0.1
DOCKER_HTTP_PROXY ?= http://172.17.0.1:7890
DOCKER_HTTPS_PROXY ?= $(DOCKER_HTTP_PROXY)
NO_PROXY ?= localhost,127.0.0.1

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

build-docker:
	docker build \
		--build-arg http_proxy=$(DOCKER_HTTP_PROXY) \
		--build-arg https_proxy=$(DOCKER_HTTPS_PROXY) \
		--build-arg no_proxy=$(NO_PROXY) \
		-t $(IMAGE_NAME):$(VERSION) .

run:
	$(PYTHON) main.py

test:
	$(PIP) install -e .
	$(PYTEST) -s	

migrate:
	$(VENV)/bin/flask db init
	$(VENV)/bin/flask db migrate -m "init tables"
	$(VENV)/bin/flask db upgrade
