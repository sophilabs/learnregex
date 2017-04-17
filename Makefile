.PHONY: clean clean-test clean-pyc clean-build help
.DEFAULT_GOAL := help
define BROWSER_PYSCRIPT
import os, webbrowser, sys
try:
	from urllib import pathname2url
except:
	from urllib.request import pathname2url

webbrowser.open("file://" + pathname2url(os.path.abspath(sys.argv[1])))
endef
export BROWSER_PYSCRIPT

define PRINT_HELP_PYSCRIPT
import re, sys

for line in sys.stdin:
	match = re.match(r'^([a-zA-Z_-]+):.*?## (.*)$$', line)
	if match:
		target, help = match.groups()
		print("%-20s %s" % (target, help))
endef
export PRINT_HELP_PYSCRIPT

BROWSER := python -c "$$BROWSER_PYSCRIPT"
VERSION=$(shell grep __version__ learnregex/__init__.py)
REQUIREMENTS="requirements_dev.pip"
TAG="\n\n\033[0;32m\#\#\# "
END=" \#\#\# \033[0m\n"

all: test

help:
	@python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

clean: clean-build clean-pyc clean-test ## remove all build, test, coverage and Python artifacts

clean-build:
	@echo $(TAG)Remove build artifacts$(END)
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +
	@echo

clean-pyc:
	@echo $(TAG)Remove Python file artifacts$(END)
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +
	@echo

clean-test:
	@echo $(TAG)Remove test and coverage artifacts$(END)
	rm -fr .tox/
	rm -f .coverage
	rm -fr htmlcov/
	@echo

lint:
	@echo $(TAG)Remove test and coverage artifacts$(END)
	flake8 learnregex tests
	@echo

msg-init:
	@echo $(TAG)Initializing messages$(END)
	pybabel init -D pyschool -i learnregex/locale/learnregex.pot -d learnregex/locale -l en
	pybabel init -D pyschool -i learnregex/locale/learnregex.pot -d learnregex/locale -l es
	@echo

msg-extract:
	@echo $(TAG)Extracting messages$(END)
	pybabel extract -o learnregex/locale/learnregex.pot learnregex
	pybabel update -D pyschool -i learnregex/locale/learnregex.pot -d learnregex/locale -l en
	pybabel update -D pyschool -i learnregex/locale/learnregex.pot -d learnregex/locale -l es
	@echo

msg-compile:
	@echo $(TAG)Compiling messages$(END)
	pybabel compile -D pyschool -d learnregex/locale -f --statistics
	@echo

msg: msg-extract msg-compile

test:
	@echo $(TAG)Run tests quickly with the default Python$(END)
	PYTHONPATH=. py.test ./tests
	@echo

test-all:
	@echo $(TAG)Run tests on every Python version with tox$(END)
	tox
	@echo

coverage:
	@echo $(TAG)Check code coverage quickly with the default Python$(END)
	coverage run --source learnregex -m pytest

		coverage report -m
		coverage html
		$(BROWSER) htmlcov/index.html
	@echo

release: clean
	@echo $(TAG)Package and upload a release$(END)
	python setup.py sdist upload
	python setup.py bdist_wheel upload
	@echo

dist: clean
	@echo $(TAG)Builds source and wheel package$(END)
	python setup.py sdist
	python setup.py bdist_wheel
	ls -l dist
	@echo

install: clean
	@echo $(TAG)Install the package to the active Python site-packages$(END)
	python setup.py install
	@echo
